# Tugas 8 Pemrograman Jaringan Kelas C
Penerapan method PUT pada web server
## Deskripsi soal
Buatlah
1. Dalam file http.py, telah ada implementasi method post yang masih kosong
2. Jalankan server pada ip 127.0.0.1 dengan port 10002
3. Bukalah browser arahkan ke http://127.0.0.1:10002/sending.html, isilah dengan sesuatu dan kirim
    - Keterangan: sending.html merupakan file dengan format HTML yang dapat digunakan untuk mengambil input dari client dan mengirimkannya ke server
4. Akan keluar tulisan ‘kosong’
5. Modifikasilah agar server dapat membalas dengan isi
    - semua  header yang dikirim dari browser
    - Yang anda isikan di form pada saat mengisi pada poin nomor 5, misalkan mengisi “ISILAH” maka server akan mereply dengan “ISILAH” juga , dan bukan ‘kosong’

Pada file server_thread_http
```
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
```
Server menerima header. Pada header mengandung informasi content length. Content length menginformasikan ukuran data pada form. Server akan terus membuka koneksi hingga semua data pada form diterima (ukuran data sama dengan nilai content length).

Pada file http_file.py
```
def http_post(self, object_address, headers):
        headers_sent = {}
        form_data = headers[-1]

        isi="<h2>header yang dikirim browser adalah :</h2>"+"<br>"

        for i in range(len(headers)):
            isi = isi+headers[i]+"<br>"
        isi = isi + "<br><h2>isi formnya adalah : </h2>"+form_data.split('=')[1]
        headers_sent['Content-type'] = 'text/html'
        # re.sub(r'+',r' ',form_data)
        return self.response(200, 'OK', isi, headers_sent)
```
Server akan mengirim balasan ke client. Isi balasan adalah seluruh header dari client dan isi form dari client. 
### Screenshot tampilan form
  <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas8/screenshots/ss_form.jpg" width="600"><br>
### Screenshot respon dari server
  <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas8/screenshots/ss_response.jpg" width="600"><br>
