import socket

HEADERSIZE = 16

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 9999))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = client.recv(16)
        if not msg:
            break
        
        if new_msg:
            try:
                msg_len = int(msg[:HEADERSIZE].strip())
                print(f"New message length: {msg[:HEADERSIZE].strip()}")
            except ValueError:
                print("Error: Invalid message length")
                break
            new_msg = False
        
        full_msg += msg.decode('utf-8')
        
        if len(full_msg) - HEADERSIZE == msg_len:
            print("Full message received")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''
            break

    if not msg:
        break

client.close()
