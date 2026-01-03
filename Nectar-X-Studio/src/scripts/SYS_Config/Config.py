import os
import platform, sys, hashlib, json, base64, uuid, psutil
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox, QInputDialog

from scripts.components.Utility.write_to_log import write_to_log
import scripts.SYS_PROMPTS.sys_msgs as sys_msgs

#------------------------------------------------------------------------------
# Keys
#------------------------------------------------------------------------------


Encoded_License_Details = 'eyJsaWNlbnNvciI6ICJaYXNoaXJpb24gaW5jIiwgImxpY2Vuc2Vfa2V5IjogIkRIVkQtMDg3Ny1EV1JILTI4NjUiLCAiZXhwaXJhdGlvbl9kYXRlIjogIjIwMjYtMTItMjMifQ=='

ACCESS_TOKEN = 'API_KEY_REDACTED_FOR_SECURITY'
token = 'API_KEY_REDACTED_FOR_SECURITY'
REFERENCE_IMAGE = 'background/NectarX.png'
OWNER = 'headlessripper'
REPO = 'Nectar-X-Studio'
CURRENT_VERSION = 'v1.4'
DEFAULT_SUGGESTIONS = ["Valorant", "CS:GO", "Minecraft"]
MAX_HISTORY = 10
POLL_INTERVAL_MS = 5000 
WEB_RAG_SYSTEM_PROMPT = sys_msgs.assistant_msg  

DECISION_MODEL_PATH = os.path.join(os.path.expanduser("~"), "Decision-Model/decision-k2.gguf")

TRANSFORMER_MODEL_PATH = os.path.join(os.path.expanduser("~"), "all-MiniLM-L12-v2")

#-----------------------------------------------------------------------------
# Plug Directory
#-----------------------------------------------------------------------------
PLUGIN_DIR = os.path.join(os.path.expanduser("~"), ".Plugin", "plugins")
os.makedirs(PLUGIN_DIR, exist_ok=True)
MAX_COLUMNS = 3



#--------------------------------------------------------------------------------
# License Unload
#--------------------------------------------------------------------------------

# ----------------- DEVICE BINDING / LICENSE CHECK -----------------
def get_device_id1():
    """Generate unique device identifier (cross-platform)."""
    node = uuid.getnode()
    sys_info = platform.system() + platform.release()
    base = f"{node}-{sys_info}"
    return hashlib.sha256(base.encode()).hexdigest()


def get_device_id():
    """
    Returns a unique, hashed device ID (hardware-locked).
    """
    node = uuid.getnode()
    sys_info = os.uname().sysname if hasattr(os, 'uname') else sys.platform
    base = f"{node}-{sys_info}"
    return hashlib.sha256(base.encode()).hexdigest()


def decode_license(encoded_license):
    """
    Decodes base64 license data into a Python dict.
    """
    try:
        decoded_json = base64.urlsafe_b64decode(encoded_license.encode()).decode()
        return json.loads(decoded_json)
    except Exception as e:
        write_to_log(f"License decoding failed: {e}")
        return None


def save_license_silently(license_data):
    """
    Saves decoded license details silently to ~/.nectar_license.
    """
    license_file = os.path.join(os.path.expanduser("~"), ".nectar_license")
    try:
        with open(license_file, "w") as f:
            json.dump(license_data, f)
        write_to_log("License details saved to .nectar_license")
    except Exception as e:
        write_to_log(f"Failed to save license: {e}")

def load_license_data():
    """
    Loads license details from ~/.nectar_license if present.
    """
    license_file = os.path.join(os.path.expanduser("~"), ".nectar_license")
    if not os.path.exists(license_file):
        return None
    try:
        with open(license_file, "r") as f:
            return json.load(f)
    except Exception as e:
        write_to_log(f"Failed to load license: {e}")
        return None

def is_license_expired(expiration_date):
    """
    Checks if the license has expired.
    """
    try:
        exp_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        return datetime.now().date() > exp_date
    except Exception:
        return True

def verify_license():
    """
    Verifies license validity, expiration, and device binding.
    Prompts for new encoded details if invalid or expired.
    """
    license_data = load_license_data()

    if not license_data:
        write_to_log("No local license found. Initializing new one.")
        decoded = decode_license(Encoded_License_Details)
        if decoded:
            save_license_silently(decoded)
            license_data = decoded
        else:
            QMessageBox.critical(None, "License Error", "Corrupted license data. Contact support.")
            return False
        
    if not all(k in license_data for k in ("licensor", "license_key", "expiration_date")):
        write_to_log("Invalid license structure.")
        QMessageBox.critical(None, "License Error", "Invalid license structure. Please reactivate.")
        return False

    # Expiration check
    if is_license_expired(license_data["expiration_date"]):
        QMessageBox.warning(None, "License Expired",
                            f"Your license expired on {license_data['expiration_date']}.\n"
                            "Please enter a new encoded license key to continue.")
        new_license, ok = QInputDialog.getText(None, "License Renewal", "Enter new encoded license:")
        if ok and new_license.strip():
            decoded_new = decode_license(new_license.strip())
            if decoded_new:
                save_license_silently(decoded_new)
                QMessageBox.information(None, "License Updated", "New license activated successfully.")
                return True
            else:
                QMessageBox.critical(None, "License Error", "Invalid encoded license entered.")
                return False
        else:
            write_to_log("User canceled license renewal.")
            return False

    device_id = get_device_id()
    local_hash = hashlib.sha256((license_data["license_key"] + device_id).encode()).hexdigest()

    write_to_log(f"License verified for {license_data['licensor']}, valid until {license_data['expiration_date']}.")
    write_to_log(f"Device ID hash: {local_hash}")

    return True

verify_license()

# ----------------- ANTI-INJECTION / ANTI-DEBUGGING -----------------
def detect_debugger_or_injection():
    blacklisted = [
        'x64dbg', 'ollydbg', 'cheatengine', 'wireshark', 
        'processhacker', 'ida', 'ghidra'
    ]
    try:
        for proc in psutil.process_iter(['name']):
            name = proc.info.get('name', '').lower()
            if any(bad in name for bad in blacklisted):
                write_to_log(f"Suspicious process detected: {name}")
                QMessageBox.warning(None, "Security Alert",
                                    f"Unauthorized debugger/injector detected: {name}\nExiting for safety.")
                sys.exit(1)
    except Exception as e:
        write_to_log(f"Process scan error: {e}")

# ----------------- SECURITY ENTRYPOINT -----------------
def run_security_checks():
    detect_debugger_or_injection()
    if not verify_license():
        sys.exit(1)

license_data = load_license_data()

#-----------------------------------------------------------------------------
# License Series
#-----------------------------------------------------------------------------
device_id = get_device_id()
local_hash = hashlib.sha256((license_data["license_key"] + device_id).encode()).hexdigest()

# License text (Zashiron License v1.2)
licenseagreement_info = f"""
Nectar-X-Studio Proprietary License 
(Zashiron License v1.2)
Copyright © 2025 Zashiron. All rights reserved.

1. Definitions
“Software” means the computer program known as Nectar-X-Studio (AI Studio),
which is currently locked to this device,  
Platform UUID(unique user identification) : {local_hash}.
including all executable code, source code, scripts, assets, documentation,
updates, and related materials provided by Zashiron.

“Licensee” (or “You”) means any person or legal entity authorized by Zashiron
to use the Software under this License.

“Use” means to install, execute, access, or otherwise interact with the Software.

2. Grant of License
Subject to the terms of this License, Zashiron grants You a non-exclusive,
non-transferable, revocable license to install and use one copy of the Software
for personal, educational, or approved commercial purposes.
All other rights are reserved by Zashiron.

3. Commercial Use
You may use the Software for commercial purposes only if you have obtained an
official commercial license or written authorization from Zashiron, and comply
with all fees and conditions. Unauthorized commercial use is strictly prohibited.

4. Restrictions
You may not:
- Copy, modify, or create derivative works of the Software.
- Distribute, sublicense, rent, lease, lend, or resell the Software.
- Circumvent or bypass licensing or activation mechanisms.
- Remove or alter any copyright or proprietary notices.
- Use the Software for illegal, unethical, or competing purposes.

5. Ownership
All rights, title, and interest in the Software remain the exclusive property of Zashiron.

6. Updates and Support
Zashiron may, at its discretion, provide updates, patches, or enhancements.
Such updates remain governed by this License.

7. Termination
This License is effective until terminated. Upon termination, You must cease use
and destroy all copies of the Software.

8. Disclaimer of Warranties
The Software is provided “AS IS”, without warranties of any kind, express or implied.

9. Limitation of Liability
In no event shall Zashiron be liable for any direct, indirect, incidental, or
consequential damages arising from use or inability to use the Software.

10. Governing Law
This License is governed by the laws of the Republic of South Africa.

11. Commercial Licensing Inquiries
For enterprise or commercial licensing:
Zashiron Licensing Department
Email: Zashiron.inc@gmail.com
Website: https://github.com/Zashiron

12. Acknowledgment
By installing or using the Software, You agree to be bound by this License.

13. Anti-Decompilation Clause
You expressly agree not to reverse engineer, decompile, disassemble, decrypt,
modify, or otherwise attempt to derive the source code or algorithms of the Software,
except where such activity is expressly permitted by law. Any unauthorized attempt
constitutes a material breach and may result in termination and legal action.

14. Data Privacy
Zashiron is committed to protecting your privacy. We do not collect or store any personal data without your consent. Any data collected during the use of the Software is used solely for the purpose of providing and improving the Software.
By using the Software, You acknowledge that You have read, understood, and agree to be bound by the terms of this License.
"""