"""Kasus 3: membaca nilai dari file. Program gagal pada file kosong / tidak ada.
Tugas: baca traceback, tentukan jenis exception, lalu rancang penanganannya."""
import os
import tempfile


def rata_rata_file(nama_file):
    with open(nama_file) as f:
        nilai = [int(baris) for baris in f]
    return sum(nilai) / len(nilai)


def coba(label, nama_file):
    try:
        print(label, "->", rata_rata_file(nama_file))
    except Exception as e:
        print(label, "-> ERROR:", type(e).__name__, "-", e)


folder = tempfile.mkdtemp()
file_ada = os.path.join(folder, "nilai.txt")
file_kosong = os.path.join(folder, "kosong.txt")
file_rusak = os.path.join(folder, "rusak.txt")
with open(file_ada, "w") as f:
    f.write("80\n90\n70\n")
open(file_kosong, "w").close()
with open(file_rusak, "w") as f:
    f.write("80\nabc\n70\n")

coba("file normal", file_ada)
coba("file kosong", file_kosong)
coba("data tidak valid", file_rusak)
coba("file tidak ada", os.path.join(folder, "tidak_ada.txt"))
