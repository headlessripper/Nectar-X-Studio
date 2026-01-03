import socket

def send_to_AlphaLLM(question):
    SERVER_ADDRESS = ('127.0.0.1', 5005)
    AUTH_KEY = "NEC-892657"

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(SERVER_ADDRESS)

        secure_message = f"{AUTH_KEY} {question}"
        client.sendall(secure_message.encode('utf-8'))

        # Stream receive loop until end marker
        full_response = []
        buffer = b''
        END_MARKER = b'<<END_OF_RESPONSE>>'
        
        while True:
            chunk = client.recv(8192)
            if not chunk:
                break  # Connection closed
            
            buffer += chunk
            # Check if end marker is in buffer
            marker_pos = buffer.find(END_MARKER)
            if marker_pos != -1:
                # Extract response before marker
                response_bytes = buffer[:marker_pos]
                full_response.append(response_bytes.decode('utf-8', errors='ignore'))
                buffer = buffer[marker_pos + len(END_MARKER):]  # Remove processed part
                break
            
            # Add complete UTF-8 chunks to response
            full_response.append(chunk.decode('utf-8', errors='ignore'))

        client.close()
        return ''.join(full_response).strip()

    except (socket.error, socket.timeout) as e:
        return f"[Error] Could not connect to AlphaLLM: {e}"
