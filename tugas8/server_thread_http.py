from socket import *
import socket
import threading
import time
import sys
import logging
from http_file import HttpServer

httpserver = HttpServer()


class ProcessTheClient(threading.Thread):
	def __init__(self, connection, address):
		self.connection = connection
		self.address = address
		threading.Thread.__init__(self)

	def run(self):
		rcv=""
		while True:
			try:
				data = self.connection.recv(1024)
				if data:
					d = data.decode()
					rcv=rcv+d
					print(repr(rcv))
					if '\r\n\r\n' in rcv:
						if 'Content-Length: ' in rcv:
							headers = rcv.split('\r\n')
							print(headers)
							expected_len = int(headers[3].split('Content-Length: ')[1])
							received_len = len(headers[-1])
							while expected_len > received_len:
								data = self.connection.recv(1024)
								d = data.decode()
								received_len+=len(d)
								rcv=rcv+d
							print(expected_len)
						#end of command, proses string
						logging.warning("data dari client: {}" . format(rcv))
						hasil = httpserver.proses(rcv)
						hasil=hasil+"\r\n\r\n"
						logging.warning("balas ke  client: {}" . format(hasil))
						self.connection.sendall(hasil.encode())
						self.connection.close()
				else:
					break
			except OSError as e:
				pass
		self.connection.close()



class Server(threading.Thread):
	def __init__(self):
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('0.0.0.0', 10002))
		self.my_socket.listen(1)
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			logging.warning("connection from {}".format(self.client_address))

			clt = ProcessTheClient(self.connection, self.client_address)
			clt.start()
			self.the_clients.append(clt)



def main():
	svr = Server()
	svr.start()

if __name__=="__main__":
	main()

