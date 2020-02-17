import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    data = connection.recv(32)
    file_name = data.decode()
    print(file_name)
    # Receive the data in small chunks and retransmit it
    f = open(file_name,'wb')
    print("receiving")
    while True:
        data = connection.recv(32)
        # print(data)
        if data:
            f.write(data)
        else:
            f.close()
            print(f"no more data from {client_address}")
            break
    # Clean up the connection
    connection.close()
