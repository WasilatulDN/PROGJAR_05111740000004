import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    indir = '.'
    file_list = list()
    file_input = ""
    print("Pilih file yang ingin anda kirim\n")
    i = 0
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if f == 'clientfile.py':
                continue
            print(str(i)+'. '+f)
            file_list.append(f)
            i+=1
    # print (file_list)
    file_input = input()
    # print(file_input)
    file_name = file_list[int(file_input)]
    sock.send(file_name.encode())
    f = open(file_name,'rb') #open in binary
    message = f.read(64) # Besar filenya yang dikirim perchunk
    print("sending")
    # print(message)
    while message:
        sock.send(message)
        message = f.read(64)

finally:
    print("closing")
    f.close()
    sock.close()
