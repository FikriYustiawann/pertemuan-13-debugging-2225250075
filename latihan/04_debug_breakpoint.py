"""Latihan 4 - Bug rata-rata (versi sudah diperbaiki).
Bug awal: pembagi tetap 5, sehingga hanya benar untuk list berisi 5 data."""


def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


tests = [
    ("T1", [80, 90, 70], 80.0),
    ("T2", [100, 80], 90.0),
    ("T3", [60, 60, 60, 60, 60], 60.0),
    ("T4", [], 0),
]
for kode, masukan, harapan in tests:
    hasil = rata_rata(masukan)
    print(kode, masukan, "expected:", harapan, "actual:", hasil,
          "PASS" if hasil == harapan else "FAIL")
