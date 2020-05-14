# Tugas 9 Pemrograman Jaringan Kelas C
Perbandingan performa server asyncronous dengan server thread
## Deskripsi soal
1. Jalankan
	- Server_async_http.py di port 45000
	- Server_thread_http.py di port 46000
2. Uji cobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi
3. Variasi konkurensi yang digunakan adalah sebagai berikut:

| Nomor | Jumlah request | konkurensi |
| --- | --- | --- |
| 1 | 1000 | 1, 10, 30, 50, 100, 300, 500, 1000 |

## Hasil pengujian asyncronous server

| No test | Concurrency level | Time taken for test [secs] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] | Time per request [ms] | Transfer rate [Kb/sec] |
| :---: |  :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 1.328 | 1000 | 0 | 122000 | 752.98 | 1.328 | 89.71 |
| 2 | 10 | 5.437 | 1000 | 0 | 122000 | 183.92 | 5.437 | 21.91 |
| 3 | 30 | 1.823 | 1000 | 0 | 122000 | 548.66 | 1.823 | 65.37 |
| 4 | 50 | 2.782 | 1000 | 0 | 122000 | 359.45 | 2.782 | 42.83 |
| 5 | 100 | 1.541 | 1000| 0 | 122000 | 649.10 | 1.541 | 77.33 |
| 6 | 300 | 0.686 | 1000 | 760 | 29402 | 1457.23 | 0.686 | 41.84 |
| 7 | 500 | 0.703 | 1000 | 182 | 23546 | 1422.25 | 0.703 | 32.70 |
| 8 | 1000 | 1.252 | 1000 | 548 | 66856 | 798.60 | 1.252 | 52.14 |

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

 
 ## Screenshot asyncronous server
- Screenshot asyncronous server konkurensi 1
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/async_1.jpg" width="600"><br>
- Screenshot asyncronous server konkurensi 10
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/async_10.jpg" width="600"><br>
- Screenshot asyncronous server konkurensi 30
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/async_30.jpg" width="600"><br>
- Screenshot asyncronous server konkurensi 50
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/async_50.jpg" width="600"><br>
- Screenshot asyncronous server konkurensi 100
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/async_100.jpg" width="600"><br>
- Screenshot asyncronous server konkurensi 300
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/async_300.jpg" width="600"><br>
- Screenshot asyncronous server konkurensi 500
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/async_500.jpg" width="600"><br>
- Screenshot asyncronous server konkurensi 1000
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/async_1000.jpg" width="600"><br>

## Screenshot thread server
- Screenshot thread server konkurensi 1
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/thread_1.jpg" width="600"><br>
- Screenshot thread server konkurensi 10
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/thread_10.jpg" width="600"><br>
- Screenshot thread server konkurensi 30
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/thread_30.jpg" width="600"><br>
- Screenshot thread server konkurensi 50
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/thread_50.jpg" width="600"><br>
- Screenshot thread server konkurensi 100
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/thread_100.jpg" width="600"><br>
- Screenshot thread server konkurensi 300
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/thread_300.jpg" width="600"><br>
- Screenshot thread server konkurensi 500
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/thread_500.jpg" width="600"><br>
- Screenshot thread server konkurensi 1000
<img src="https://github.com/WasilatulDN/PROGJAR_05111740000004/blob/master/tugas9/screenshots/thread_1000.jpg" width="600"><br>