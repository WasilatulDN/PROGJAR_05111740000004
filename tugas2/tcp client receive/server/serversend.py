import sys
import socket
import os
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
indir = "."
while True:
    # Wait for a connection
    file_list = list()
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    message = "Pilih file yang anda ingin download\n"
    i = 0
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if f == 'serversend.py':
                continue
            message+=str(i)+". "+f+"\n"
            file_list.append(f)
            i+=1
    message_len = len(message)
    message = str(message_len) + ';' + message
    connection.sendall(message.encode())
    print("---DATA SENT---\n"+message)
    print("--- WAITING FOR INPUT ---")
    data = connection.recv(8)
    file_input = data.decode()
    file_name = file_list[int(file_input)]

    file_name_len = len(file_name)
    message = str(file_name_len) + ';' + file_name
    # print(message)
    connection.sendall(message.encode())
    header_file = None
    f = open(file_name,'rb') #open in binary
    # message = f.read(64) # Besar filenya yang dikirim perchunk
    if header_file is None:
        byte_len = os.stat(file_name).st_size
        print(byte_len)
        message_header = str(byte_len)
        # print(message_header.encode())
        connection.send(message_header.encode())
        flag = 0
    while flag == 0:
        flag = connection.recv(8).decode()
    while message:
        message = f.read(64)
        connection.send(message)
    print("closing")
    f.close()
    # Clean up the connection
    connection.close()
