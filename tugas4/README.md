# Tugas 4 Pemrograman Jaringan Kelas C
Membuat file transfer protokol
## Deskripsi soal
1. Rancanglah sebuah protokol untuk
   - Meletakkan file
   - Mengambil file
   - Melihat list file
2. Buatlah dokumentasi dari protokol tersebut berisikan
   - Ketentuan membaca format
   - Daftar fitur
   - Cara melakukan request
   - Apa respon yang didapat
3. Gunakan format JSON untuk tugas ini
4. Buatlah client untuk operasi tersebut
## Dokumentasi
1. Ketentuan membaca format<br>
Seluruh komunikasi antara server dan client (request dan response) menggunakan format JSON. Format yang digunakan mengikuti aturan sebagai berikut :
    ```
    {
        'type' : "Berisi tipe content"
        'content' : "Body dari request/response"
    }
    ```
    Terdapat empat tipe konten. Tipe konten memengaruhi bagaimana request atau response tersebut diperlakukan. Empat tipe konten tersebut yaitu :
    - Command<br>
      Tipe command akan diperlakukan sesuai dengan konten commandnya. Digunakan oleh client saat mengirim **request** ke server. Command yang tersedia untuk dikirim ke server adalah **get, lss, help, dan exit**. Sehingga format JSON yang digunakan adalah sebagai berikut :
       ```
      {
          'type' : "command"
          'content' : "get <no> / lss / help / exit"
      }
      ```
    - Message<br>
      Tipe message akan diperlakukan dengan menampilkan kontennya ke layar. Digunakan oleh server saat mengirim **response** ke client. Server akan mengirim message untuk command **lss dan help**. Sehingga format JSON yang digunakan adalah sebagai berikut :
       ```
      {
          'type' : "message"
          'content' : "teks cara menggunakan protokol atau list daftar file pada server"
      }
      ```
    - File<br>
      Tipe file akan diperlakukan dengan menuliskan kontennya ke file binary. Digunakan untuk pengiriman **file** baik dari server ke client maupun client ke server. Untuk pengiriman server ke client digunakan pada saat client mengambil (download) file dari server sebagai response dari command **get**. Sedangkan untuk pengiriman client ke server digunakan pada saat client meletakkan (upload) file ke server meggunakan command **put**. Sehingga format JSON yang digunakan adalah sebagai berikut :
       ```
      {
          'type' : "file"
          'content' : {
                          'filename' : nama file,
                          'data' : base64 dari binary isi file
                      }
      }
      ```
    - Terminate<br>
      Tipe command akan diperlakukan dengan mengakhiri koneksi client dengan server. Digunakan oleh server saat mengirim response ke client khusus untuk command **exit**. Sehingga format JSON yang digunakan adalah sebagai berikut :
       ```
      {
          'type' : "terminate"
          'content' : "terminate"
      }
      ```

2. Daftar fitur
   - help<br>
     Digunakan untuk menampilkan daftar command yang bisa dilakukan oleh client beserta kegunaan dari command tersebut.<br>
     Format request (dikirim ke server) :
      ```
      {
          'type' : "command"
          'content' : "help"
      }
      ```
      Format response (diterima oleh client) :
      ```
      {
          'type' : "message"
          'content' : teks cara menggunakan protokol
      }
      ```
   - lss<br>
     Digunakan untuk menampilkan daftar file yang ada pada server.<br>
     Format request (dikirim ke server) :
      ```
      {
          'type' : "command"
          'content' : "lss"
      }
      ```
      Format response (diterima oleh client) :
      ```
      {
          'type' : "message"
          'content' : list file pada server
      }
      ```
   - get<br>
     Digunakan untuk mengambil (download) file dari server.<br>
     Format request (dikirim ke server) :
      ```
      {
          'type' : "command"
          'content' : "get <no>"
      }
      ```
      Format response (diterima oleh client) :
      ```
      {
          'type' : "file"
          'content' : {
                          'filename' : nama file,
                          'data' : base64 dari binary isi file
                      }
      }
      ```
   - exit<br>
     Digunakan untuk memutus koneksi dengan server.<br>
     Format request (dikirim ke server) :
      ```
      {
          'type' : "command"
          'content' : "exit"
      }
      ```
      Format response (diterima oleh client) :
      ```
      {
          'type' : "terminate"
          'content' : "terminate"
      }
      ```
   - ls<br>
     Digunakan untuk menampilkan daftar file yang ada pada client. ls merupakan command lokal (tidak dikirim ke server).<br>
     Format request (tidak dikirim ke server) :
      ```
      ls
      ```
      Format response : list file pada client.
   - put<br>
     Digunakan untuk meletakkan (upload) file ke server.<br>
     Format request (tidak dikirim ke server) :
      ```
      put <no>
      ```
      Format request yang dikirim ke server :
      ```
      {
          'type' : "file"
          'content' : {
                          'filename' : nama file,
                          'data' : base64 dari binary isi file
                      }
      }
      ```
3. cara melakukan request dan responsenya
   - help<br>
     Cara melakukan request :
     - pastikan server.py telah berjalan.
     - jalankan client.py.
     - ketikkan 'help' pada terminal tanpa menggunakan tanda petik ' '
     
     Response :<br>
     Berikut screenshot request help dan responsenya.<br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/help.jpg" width="600"><br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/help_json.jpg" width="600">
   - lss<br>
     Cara melakukan request :
     - pastikan server.py telah berjalan.
     - jalankan client.py.
     - ketikkan 'lss' pada terminal tanpa menggunakan tanda petik ' '
     
     Response :<br>
     Berikut screenshot request lss dan responsenya.<br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/lss.jpg" width="600"><br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/lss_json.jpg" width="600">
   - get<br>
     Cara melakukan request :
     - pastikan server.py telah berjalan.
     - jalankan client.py.
     - ketikkan 'get < no >' pada terminal tanpa menggunakan tanda petik ' '. < no > berisi nomor urutan file berdasarkan response lss. Misal 'get 2'
     
     Response :<br>
     Berikut screenshot request get dan responsenya.<br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/get.jpg" width="600"><br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/get_2.jpg" width="600"><br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/get_json.jpg" width="600">
   - exit<br>
     Cara melakukan request :
     - pastikan server.py telah berjalan.
     - jalankan client.py.
     - ketikkan 'exit' pada terminal tanpa menggunakan tanda petik ' '
     
     Response :<br>
     Berikut screenshot request exit dan responsenya.<br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/exit.jpg" width="600"><br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/exit_json.jpg" width="600">
   - ls<br>
     Cara melakukan request :
     - pastikan server.py telah berjalan.
     - jalankan client.py.
     - ketikkan 'ls' pada terminal tanpa menggunakan tanda petik ' '
     
     Response :<br>
     Berikut screenshot request ls dan responsenya.<br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/ls.jpg" width="600">
   - put<br>
     Cara melakukan request :
     - pastikan server.py telah berjalan.
     - jalankan client.py.
     - ketikkan 'put < no >' pada terminal tanpa menggunakan tanda petik ' '. < no > berisi nomor urutan file berdasarkan response ls. Misal 'put 2'
     
     Response :<br>
     Berikut screenshot request put dan responsenya.<br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/put.jpg" width="600"><br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/put_2.jpg" width="600"><br>
     <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas4/screenshots/put_json.jpg" width="600">
