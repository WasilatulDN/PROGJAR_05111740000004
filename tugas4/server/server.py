import socket
import json
import os
import base64
import threading

# Threading class

class Server(threading.Thread):
	def __init__(self):
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('0.0.0.0',10000))
		self.my_socket.listen(1)
		print(f"starting up on server")
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			print(f"connection from {self.client_address}")
			clt = ProcessTheClient(self.connection, self.client_address)
			clt.start()
			self.the_clients.append(clt)

class ProcessTheClient(threading.Thread):
	def __init__(self,connection,address):
		self.indir = '.'
		self.connection = connection
		self.address = address
		self.file_list = list()
		self.file_names = ''
		threading.Thread.__init__(self)

	def run(self):
		message = self.prepareMessage('Protokol WFTP (VER α-ARI). Ketik `help` untuk melihat daftar command. Ketik `exit` untuk memutus koneksi.')
		self.sendMessage(message)
		while True:
			response_json = self.receiveMessage()
			response = json.loads(response_json)
			if response['type'] == 'command':
				content,msg_type = self.executeCommand(response['content'])
				message = self.prepareMessage(content,msg_type=msg_type)
				self.sendMessage(message)
				if msg_type == 'terminate':
					self.connection.close()
					break
			if response['type'] == 'file':
				filedata = json.loads(response['content'])
				binarystream = open(filedata['filename'],'wb')
				binarystream.write(base64.b64decode(filedata['data'].encode()))
				binarystream.close()

	def sendMessage(self,message:str):
		connection = self.connection
		print('dikirim : ')
		print(message)
		connection.sendall(message.encode())
		connection.sendall(b'*done*')
		return

	def prepareMessage(self,message:str, msg_type:str = 'message') -> str:
		message_dict = {
			'type': msg_type,
			'content': message
		}
		message_json = json.dumps(message_dict)
		return message_json

	def receiveMessage(self)->str :
		connection = self.connection
		message = b''
		while True:
			if not message.decode()[-6:] == '*done*' :
				data = connection.recv(32)
				message+=data
			else:
				break
		print('diterima : ')
		print(message[:-6])
		return message.decode()[:-6]

	def updateFileList(self)->None:
		self.file_list = list()
		self.file_names = ''
		i = 1
		for root, dirs, filenames in os.walk(self.indir):
			for f in filenames:
				if f == 'server.py':
					continue
				self.file_names+=str(i)+". "+f+"\n"
				self.file_list.append(f)
				i += 1

	def executeCommand(self,command:str)->str:
		self.updateFileList()
		command = command.split(' ')
		args = ''
		# print(command)
		if len(command) > 1:
			args = command[1]
		# print(command,args)
		command = command[0]
		if command == 'lss':
			message = self.file_names
			msg_type = 'message'
		elif command == 'help':
			message ='''
			WASILATUL FILE TRANSFER PROTOCOL (VER α-ARI)
			help		menampilkan list command
			lss			menampilkan list file di server
			ls		  	menampilkan list file di lokal
			get <no>	download file urutan ke <no> berdasarkan lss
			put <no>	upload file urutan ke <no> berdasarkan ls
			exit		memutus koneksi dengan server
			'''
			msg_type = 'message'
		elif command == 'get':
			# print(self.file_list, args)
			filename = self.file_list[int(args)-1]
			filedata = {
				'filename': filename,
				'data' : b''
			}
			binarystream = open(filename, 'rb')
			image = binarystream.read()
			filedata['data'] = base64.b64encode(image).decode()
			binarystream.close()
			message = json.dumps(filedata)
			# print(message)
			msg_type = 'file'
		elif command == 'exit':
			message = 'terminate'
			msg_type = 'terminate'
		return[message, msg_type]

if __name__== "__main__":
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	srv = Server()
	srv.start()