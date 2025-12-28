global _logger_initialized 
import threading
import logging
import os

#-----------------------------------------------------------------------------
# Logger Setup
#-----------------------------------------------------------------------------

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

_logger_lock = threading.Lock()
_logger_initialized = False

def setup_logger(log_file_path='logs/Debug.log'):
    global _logger_initialized
    with _logger_lock:
        if _logger_initialized:
            return
        try:
            log_dir = os.path.dirname(log_file_path)
            if log_dir:
                try:
                    os.makedirs(log_dir, exist_ok=True)
                except Exception:
                    log_file_path = os.path.basename(log_file_path)

            try:
                logging.basicConfig(
                    filename=log_file_path,
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    encoding='utf-8'
                )
            except Exception:
                logging.basicConfig(
                    filename=log_file_path,
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )

            logging.raiseExceptions = False
            logging.debug('Logger initialized successfully.')
            _logger_initialized = True

        except Exception as e:
            write_to_log(f"Logger initialization failed: {e}")
            _logger_initialized = True

setup_logger()

def write_log(message: str, level=logging.DEBUG):
    try:
        if not _logger_initialized:
            setup_logger()
        logging.log(level, message)
    except Exception:
        pass
setup_logger()
from datetime import datetime

def write_to_log(message: str, file_path: str='Nectar-Studio.log'):
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
    timestamped_message = f'[{datetime.now().isoformat()}] {message}\n'
    with open(file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(timestamped_message)
