"""Kasus 1: program berjalan tanpa error, tetapi hasil untuk nilai 60 salah.
Tugas: rancang test case 59, 60, 61 lalu temukan penyebabnya."""


def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


for n in [75, 60, 59]:
    print(n, "->", status_lulus(n))
