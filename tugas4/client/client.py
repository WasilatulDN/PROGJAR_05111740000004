import socket
import json
import os
import base64

# Global variable
file_list = list()
file_names = ''

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

# Core function

def receiveMessage()->str :
    message = b''
    while True:
        if not message.decode()[-6:] == '*done*':
            data = sock.recv(16)
            message += data
        else:
            break
    return message.decode()[:-6]

def prepareMessage(message:str, res_type:str = 'command') -> str:
    message_dict = {
        'type': res_type,
        'content': message
    }
    message_json = json.dumps(message_dict)
    return message_json

def sendMessage(message:str):
    sock.sendall(message.encode())
    sock.sendall(b'*done*')
    return

def executeCommand(message:str):
    message_dict = json.loads(message)
    if message_dict['type'] == 'message':
        print(message_dict['content'])
        pass
    elif message_dict['type'] == 'file':
        filedata = json.loads(message_dict['content'])
        binarystream = open(filedata['filename'], 'wb')
        binarystream.write(base64.b64decode(filedata['data'].encode()))
        binarystream.close()
    elif message_dict['type'] == 'terminate':
        print('connection is closed')
        exit()
    return

def updateFileList()->None:
    global file_list, file_names
    file_list = list()
    file_names = ''
    i = 1
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if f == 'client.py':
                continue
            file_names+=str(i)+". "+f+"\n"
            file_list.append(f)
            i += 1

def getFileNames()->str:
    global file_names
    return file_names

if __name__== "__main__":
    terminate = 1
    indir = '.'
    message = receiveMessage()
    message_dict = json.loads(message)
    print(message_dict['content'])
    while terminate:
        responses = input()
        updateFileList()
        response = responses.split(' ')
        args = None
        if len(response) > 1:
            args = response[1]
        response = response[0]
        if response == 'put':
            try:
                filename = file_list[int(args)-1]
                filedata = {
                    'filename': filename,
                    'data' : b''
                }
                binarystream = open(filename, 'rb')
                image = binarystream.read()
                filedata['data'] = base64.b64encode(image).decode()
                binarystream.close()
                response = json.dumps(filedata)
                res_type = 'file'
                message = prepareMessage(response, res_type=res_type)
                # print(message)
                sendMessage(message)
                print('File berhasil dikirim ke server')
            except Exception as e:
                print('Error dalam penyiapan file')
                print(e)
        elif response == 'ls':
            message = getFileNames()
            print(message)
        elif response == 'help' or response == 'exit' or response == 'lss':
            message = prepareMessage(response)
            sendMessage(message)
            message = receiveMessage()
            executeCommand(message)
        elif response == 'get':
            message = prepareMessage(responses)
            sendMessage(message)
            message = receiveMessage()
            executeCommand(message)
            print('File berhasil diunduh dari server')
        else:
            print('Command tidak ditemukan!')