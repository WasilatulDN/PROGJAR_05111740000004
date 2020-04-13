import sys
import os.path
import uuid
from glob import glob
from datetime import datetime

class HttpServer:
	# Format RFC2616Connection: close
	# HTTP/1.0 CODE RESPONSE_MESSAGE
	# Content-Length: 
	# Content-type: 
	# Date: 
	# Server: 
	def response(self,kode=404,message='Not Found',messagebody='',headers={}):
		tanggal = datetime.now().strftime('%c')
		resp=[]
		resp.append("HTTP/1.0 {} {}\r\n" . format(kode,message))
		resp.append("Date: {}\r\n" . format(tanggal))
		resp.append("Connection: close\r\n")
		resp.append("Server: wasil/1.0 (alphaari)\r\n")
		resp.append("Content-Length: {}\r\n" . format(len(messagebody)))
		for kk in headers:
			resp.append("{}:{}\r\n" . format(kk,headers[kk]))
		resp.append("\r\n")
		resp.append("{}" . format(messagebody))
		response_str=''
		for i in resp:	
			response_str="{}{}" . format(response_str,i)
		print(type(response_str))
		return response_str

	def proses(self,data):
		# data = data.decode()
		requests = data.split("\r\n")
		baris = requests[0]

		j = baris.split(" ")
		try:
			method=j[0].upper().strip()
			if (method=='GET'):
				return self.http_response()
			else:
				return self.response(400,'Bad Request','',{})
		except IndexError:
			return self.response(400,'Bad Request','',{})
	def http_response(self):
		isi = "<h1>SERVER HTTP</h1>"
		
		headers={}
		headers['Content-type']='text/html'
		
		return self.response(200,'OK',isi,headers)
		















