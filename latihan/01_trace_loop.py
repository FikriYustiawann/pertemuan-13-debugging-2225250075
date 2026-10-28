"""Latihan 1 - Tracing perulangan.
Prediksi: total=1; i=1->1, i=2->2, i=3->6, i=4->24  => output 24

Langkah | i | total sebelum | total sesudah
   1    | 1 |       1       |      1
   2    | 2 |       1       |      2
   3    | 3 |       2       |      6
   4    | 4 |       6       |     24
"""
total = 1
for i in range(1, 5):
    total = total * i
    print("i =", i, "total =", total)  # print sementara untuk verifikasi tracing
print(total)
