# Tugas 10 Pemrograman Jaringan Kelas C
Perbandingan performa server asyncronous menggunakan load balancer dengan server thread
## Deskripsi soal
1. Jalankan async_server.py pada port 9002, 9003, 9004, 9005 (lihat pada BackendList)
2. Jalankan file lb.py, jalankan di port 44444
3. Jalankan browser, akseslah http://localhost:44444/page.html
4. Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian
5. Lakukan performance test dengan parameter sebagai berikut:

| Nomor | Jumlah request | konkurensi |
| --- | --- | --- |
| 1 | 1000 | 1, 10, 30, 50, 100, 300, 500, 1000 |

## Hasil pengujian asyncronous server dengan load balancer

| No test | Concurrency level | Time taken for test [secs] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] | Time per request [ms] | Transfer rate [Kb/sec] |
| :---: |  :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 6.347 | 1000 | 0 | 122000 | 157.57 | 6.347 | 18.77 |
| 2 | 10 | 4.315 | 1000 | 0 | 122000 | 231.77 | 4.315 | 27.61 |
| 3 | 30 | 3.994 | 1000 | 0 | 122000 | 250.39 | 3.994 | 29.83 |
| 4 | 50 | 3.022 | 1000 | 0 | 122000 | 330.86 | 3.022 | 39.42 |
| 5 | 100 | 2.354 | 1000| 0 | 122000 | 424.86 | 2.354 | 50.62 |
| 6 | 300 | 1.479 | 1000 | 505 | 61610 | 675.90 | 1.479 | 40.67 |
| 7 | 500 | 1.151 | 1000 | 362 | 45140 | 868.82 | 1.151 | 38.30 |
| 8 | 1000 | 1.071 | 1000 | 285 | 34770 | 933.68 | 1.071 | 31.70 |

## Hasil pengujian thread server

| No test | Concurrency level | Time taken for test [secs] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] | Time per request [ms] | Transfer rate [Kb/sec] |
| :---: |  :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 1132.270 | 1000 | 0 | 122000 | 0.88 | 1132.270 | 0.11 |
| 2 | 10 | 455.915 | 1000 | 0 | 122000 | 2.19 | 455.915 | 0.26 |
| 3 | 30 | 492.000 | 1000 | 0 | 122000 | 2.03 | 492.000 | 0.24 |
| 4 | 50 | 445.714 | 1000 | 0 | 122000 | 2.24 | 445.714 | 0.27 |
| 5 | 100 | 445.135 | 1000| 0 | 122000 | 2.25 | 445.135 | 0.27 |
| 6 | 300 | 11.843 | 1000 | 700 | 36600 | 84.44 | 11.843 | 3.02 |
| 7 | 500 | 33.643 | 1000 | 449 | 54778 | 29.72 | 33.643 | 1.59 |
| 8 | 1000 | 198.961 | 1000 | 796 | 97112 | 9.18 | 108.961 | 0.87 |

 
 ## Screenshot halaman web
 <img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/ss_web.jpg" width="600"><br>

 ## Screenshot load balancer
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/ss_log.jpg" width="600"><br>

 ## Screenshot asyncronous server dengan load balancer
- Screenshot asyncronous server dengan load balancer konkurensi 1
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/async_1.jpg" width="600"><br>
- Screenshot asyncronous server dengan load balancer konkurensi 10
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/async_10.jpg" width="600"><br>
- Screenshot asyncronous server dengan load balancer konkurensi 30
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/async_30.jpg" width="600"><br>
- Screenshot asyncronous server dengan load balancer konkurensi 50
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/async_50.jpg" width="600"><br>
- Screenshot asyncronous server dengan load balancer konkurensi 100
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/async_100.jpg" width="600"><br>
- Screenshot asyncronous server dengan load balancer konkurensi 300
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/async_300.jpg" width="600"><br>
- Screenshot asyncronous server dengan load balancer konkurensi 500
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/async_500.jpg" width="600"><br>
- Screenshot asyncronous server dengan load balancer konkurensi 1000
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/async_1000.jpg" width="600"><br>

## Screenshot thread server
- Screenshot thread server konkurensi 1
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/thread_1.jpg" width="600"><br>
- Screenshot thread server konkurensi 10
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/thread_10.jpg" width="600"><br>
- Screenshot thread server konkurensi 30
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/thread_30.jpg" width="600"><br>
- Screenshot thread server konkurensi 50
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/thread_50.jpg" width="600"><br>
- Screenshot thread server konkurensi 100
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/thread_100.jpg" width="600"><br>
- Screenshot thread server konkurensi 300
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/thread_300.jpg" width="600"><br>
- Screenshot thread server konkurensi 500
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/thread_500.jpg" width="600"><br>
- Screenshot thread server konkurensi 1000
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas10/screenshots/thread_1000.jpg" width="600"><br>