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

## Hasil pengujian

| No test | Total request | Concurrency level | Time taken for test [secs] | Complete request | Failed request | Total transferred [bytes] | Request per second [#/sec] | Time per request [ms] | Time per request* [ms] | Transfer rate [Kb/sec] |
| :---: |  :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 10 | 1 | 0.136 | 10 | 0 | 1680 | 73.61 | 13.585 | 13.585 | 12.08 |
| 2 | 10 | 5 | 1.218 | 10 | 0 | 1680 | 8.21 | 609.247 | 121.849 | 1.35 |
| 3 | 10 | 10 | 1.838 | 10 | 0 | 1680 | 5.44 | 1837.792 | 183.779 | 0.89 |
| 4 | 50 | 1 | 11.085 | 50 | 0 | 8400 | 4.51 | 221.699 | 221.699 | 0.74 |
| 5 | 50 | 10 | 3.033 | 50 | 0 | 8400 | 16.49 | 606.509 | 60.651 | 2.71 |
| 6 | 50 | 30 | 33.115 | 50 | 0 | 8400 | 1.51 | 19869.009 | 662.300 | 0.25 |
| 7 | 50 | 50 | 4.314 | 50 | 0 | 8400 | 11.59 | 4314.013 | 86.280 | 1.90 |
| 8 | 100 | 1 | 20.310 | 100 | 0 | 16800 | 4.92 | 203.101 | 203.101 | 0.81 |
| 9 | 100 | 10 | 46.184 | 100 | 0 | 16800 | 2.17 | 4618.442 | 461.844 | 0.36 |
| 10 | 100 | 50 | 20.714 | 100 | 0 | 16800 | 4.83 | 10356.801 | 207.136 | 0.79 |
| 11 | 100 | 100 | 48.288 | 100 | 0 | 16800 | 2.07 | 48288.315 | 482.883 | 0.34 |
