import socket 

# ----------------------------
# Find a free port
# ----------------------------
def find_free_port():
    """Find a free local port to use for the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]