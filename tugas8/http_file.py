import sys
import os.path
import re
import uuid
from glob import glob
from datetime import datetime


class HttpServer:
    def __init__(self):
        self.sessions = {}
        self.types = {}
        self.types['.pdf'] = 'application/pdf'
        self.types['.jpg'] = 'image/jpeg'
        self.types['.txt'] = 'text/plain'
        self.types['.html'] = 'text/html'

    def response(self, kode=404, message='Not Found', messagebody='', headers={}):
        tanggal = datetime.now().strftime('%c')
        resp = []
        resp.append("HTTP/1.0 {} {}\r\n".format(kode, message))
        resp.append("Date: {}\r\n".format(tanggal))
        resp.append("Connection: close\r\n")
        resp.append("Server: myserver/1.0\r\n")
        resp.append("Content-Length: {}\r\n".format(len(messagebody)))
        for kk in headers:
            resp.append("{}:{}\r\n".format(kk, headers[kk]))
        resp.append("\r\n")
        resp.append("{}".format(messagebody))
        response_str = ''
        for i in resp:
            response_str = "{}{}".format(response_str, i)
        return response_str

    def proses(self, data):

        requests = data.split("\r\n")
        # print(requests)

        baris = requests[0]
        # print(baris)

        all_headers = [n for n in requests[1:] if n != '']
        print(all_headers)

        j = baris.split(" ")
        try:
            method = j[0].upper().strip()
            if (method == 'GET'):
                object_address = j[1].strip()
                return self.http_get(object_address, all_headers)
            if (method == 'POST'):
                print(j)
                object_address = j[1].strip()
                return self.http_post(object_address, all_headers)
            else:
                return self.response(400, 'Bad Request', '', {})
        except IndexError:
            return self.response(400, 'Bad Request', '', {})

    def http_get(self, object_address, headers):
        files = glob('./*')
        thedir = '.\\'
        object = object_address.split("/")[1]
        print(files)
        print(thedir + object)
        print(files[1])
        if thedir + object not in files:
            return self.response(404, 'Not Found', '', {})
        fp = open(thedir + object, 'r')
        isi = fp.read()

        fext = os.path.splitext(thedir + object)[1]
        content_type = self.types[fext]

        headers = {}
        headers['Content-type'] = content_type

        return self.response(200, 'OK', isi, headers)

    def http_post(self, object_address, headers):
        headers_sent = {}
        form_data = headers[-1]
        print('form_data')
        print(form_data)
        print(len(headers))
        # print('object_address')
        # print(object_address)
        # print('headers')
        # print(headers)
        # header = headers.split('\r\n')
        isi="<h2>header yang dikirim browser adalah :</h2>"+"<br>"

        # print(isi)
        for i in range(len(headers)):
            isi = isi+headers[i]+"<br>"
        isi = isi + "<br><h2>isi formnya adalah : </h2>"+form_data.split('=')[1]
        headers_sent['Content-type'] = 'text/html'
        # re.sub(r'+',r' ',form_data)
        return self.response(200, 'OK', isi, headers_sent)


# >>> import os.path
# >>> ext = os.path.splitext('/ak/52.png')

if __name__ == "__main__":
    httpserver = HttpServer()
    d = httpserver.proses('GET testing.txt HTTP/1.0')
    print(d)
    d = httpserver.http_get('testing2.txt')
    print(d)
    d = httpserver.http_get('testing.txt')
    print(d)
