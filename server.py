import socket

HEADERSIZE = 16

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 9999))
server.listen(5)
print(f"Server listening at port {9999}")

while True:
    client_socket, address = server.accept()
    print(f"Connection from {address} has been established")
    
    
    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg
    
    client_socket.send(bytes(msg, "utf-8"))
