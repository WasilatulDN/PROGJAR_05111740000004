# Tugas 7 Pemrograman Jaringan Kelas C
Melakukan performance test sederhana
## Deskripsi soal
Performance test sederhana, hanya bisa dilakukan di linux/unix based
1. Gunakan apachebenchark , dengan command ab
2. Testlah server anda dengan : ab -n \<jumlahrequest> -c \<concurency> http://127.0.0.1:10001/ dengan parameter sbb:

| Nomor | Jumlah request | konkurensi |
| --- | --- | --- |
| 1 | 10 | 1,5,10 |
| 1 | 50 | 1,10,30,50 |
| 1 | 100 | 1,10,50,100 |
