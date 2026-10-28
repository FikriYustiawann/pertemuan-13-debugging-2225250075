"""Menjalankan seluruh test case Praktik 4.
Cara: python3 praktik/uji_praktik_4.py"""
import contextlib
import io
import sys

# Impor tanpa menampilkan print bawaan dari praktik_4_debugging.py
with contextlib.redirect_stdout(io.StringIO()):
    from praktik_4_debugging import hitung_rata_rata, status, nilai_tertinggi

tests = [
    ("T1", "rata-rata", hitung_rata_rata, [80, 60, 90, 70], 75.0),
    ("T2", "rata-rata", hitung_rata_rata, [100, 80], 90.0),
    ("T3", "status", status, 60, "Lulus"),
    ("T4", "status", status, 59, "Tidak lulus"),
    ("T5", "tertinggi", nilai_tertinggi, [80, 60, 90, 70], 90),
    ("T6", "rata-rata kosong", hitung_rata_rata, [], 0),
    ("T7", "tertinggi kosong", nilai_tertinggi, [], None),
    ("T8", "tertinggi negatif", nilai_tertinggi, [-5, -2, -9], -2),
]

gagal = 0
print(f"{'ID':<4}{'Target':<19}{'Input':<20}{'Expected':<13}{'Actual':<13}Status")
for kode, target, fungsi, masukan, harapan in tests:
    try:
        hasil = fungsi(masukan)
    except Exception as e:
        hasil = type(e).__name__
    ok = hasil == harapan
    gagal += not ok
    print(f"{kode:<4}{target:<19}{str(masukan):<20}{str(harapan):<13}{str(hasil):<13}{'PASS' if ok else 'FAIL'}")

print(f"\nRingkasan: {len(tests) - gagal}/{len(tests)} PASS")
sys.exit(1 if gagal else 0)
