import socket

#--------------------------------------------------------------------------------
# Send Function
#--------------------------------------------------------------------------------

def send_to_AlphaLLM(question):
    import socket
    
    SERVER_ADDRESS = ('127.0.0.1', 5005)
    AUTH_KEY = ("NEC-892657")

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
        client.connect(SERVER_ADDRESS)

        secure_message = f"{AUTH_KEY} {question}"
        client.sendall(secure_message.encode('utf-8'))

        response = client.recv(8192).decode('utf-8').strip()
        client.close()

        return response

    except (socket.error, socket.timeout) as e:
        return f"[Error] Could not connect to AlphaLLM: {e}"