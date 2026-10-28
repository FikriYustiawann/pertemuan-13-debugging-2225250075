"""Latihan 3 - Bug batas kelulusan (versi sudah diperbaiki: > menjadi >=)."""


def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


tests = [("T1", 59, "Tidak lulus"), ("T2", 60, "Lulus"), ("T3", 61, "Lulus")]
for kode, masukan, harapan in tests:
    hasil = status_lulus(masukan)
    print(kode, masukan, "expected:", harapan, "actual:", hasil,
          "PASS" if hasil == harapan else "FAIL")
