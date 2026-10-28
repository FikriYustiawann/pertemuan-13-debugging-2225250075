"""Kasus 2: hasil benar untuk satu data, tetapi salah untuk data lain.
Tugas: jelaskan mengapa, lalu uji dengan list berbeda panjang."""


def rata_rata(data):
    total = sum(data)
    return total / 5


print(rata_rata([80, 90, 70]))
