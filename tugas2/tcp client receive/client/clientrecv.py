import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)


try:
    expected_message = None
    received_message = 0
    received = b""
    while True:
        if expected_message is None:
            data = sock.recv(32)
            temp_message = data.decode()
            splited_message = temp_message.split(';')
            expected_message = int(splited_message[0])
            temp_recv = ''
            for i in range(1,len(splited_message)):
                temp_recv += splited_message[i]
            received += temp_recv.encode()
            received_message += len(temp_recv.encode())
        elif received_message < expected_message:
            data = sock.recv(32)
            received += data
            received_message += len(data)
            # print (received)
        else:
            break

    print(received.decode())
    file_input = input()
    sock.send(file_input.encode())
    filename = b""
    
    expected_message = None
    received_message = 0
    
    while True:
        if expected_message is None:
            data = sock.recv(32)
            temp_message = data.decode()
            splited_message = temp_message.split(';')
            expected_message = int(splited_message[0])
            temp_recv = ''
            for i in range(1,len(splited_message)):
                temp_recv += splited_message[i]
            filename += temp_recv.encode()
            received_message += len(temp_recv.encode())
        elif received_message < expected_message:
            data = sock.recv(32)
            filename += data
            received_message += len(data)
            # print (received)
        else:
            break
        
    filename = filename.decode()
    # print(filename)
    f = open(filename,'wb')
    
    expected_message = None
    received_message = 0
    print("downloading")
    while True:
        if expected_message is None:
            data = sock.recv(8)
            # print(data)
            temp_message = data.decode()
            expected_message = int(temp_message)
            print(expected_message)
            message = "ACK"
            sock.send(message.encode())
        elif received_message < expected_message:
            data = sock.recv(64)
            f.write(data)
            received_message += len(data)
            # print (received)
        else:
            f.close()
            break

finally:
    print("closing")
    sock.close()
