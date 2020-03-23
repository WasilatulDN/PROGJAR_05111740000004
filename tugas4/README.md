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
    Terdapat empat tipe konten yaitu :
    - Command
      Digunakan oleh client saat mengirim **request** ke server. Command yang tersedia untuk dikirim ke server adalah **get, lss, help, dan exit**. Sehingga format JSON yang digunakan adalah sebagai berikut :
       ```
      {
          'type' : "command"
          'content' : "get <no> / lss / help / exit"
      }
      ```
    - Message
      Digunakan oleh server saat mengirim **response** ke client. Server akan mengirim message untuk command **lss dan help**. Sehingga format JSON yang digunakan adalah sebagai berikut :
       ```
      {
          'type' : "message"
          'content' : "teks cara menggunakan protokol atau list daftar file pada server"
      }
      ```
    - File
      Digunakan untuk pengiriman **file** baik dari server ke client maupun client ke server. Untuk pengiriman server ke client digunakan pada saat client mengambil (download) file dari server sebagai response dari command **get**. Sedangkan untuk pengiriman client ke server digunakan pada saat client meletakkan (upload) file ke server meggunakan command **put**. Sehingga format JSON yang digunakan adalah sebagai berikut :
       ```
      {
          'type' : "file"
          'content' : {
                          'filename' : nama file,
                          'data' : base64 dari binary isi file
                      }
      }
      ```
    - Terminate
      Digunakan oleh server saat mengirim response ke client khusus untuk command exit. Sehingga format JSON yang digunakan adalah sebagai berikut :
       ```
      {
          'type' : "terminate"
          'content' : "terminate"
      }
      ```

2. Daftar fitur, cara melakukan request dan responsenya
