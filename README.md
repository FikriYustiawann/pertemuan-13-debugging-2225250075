# Pertemuan 13 - Debugging dan Testing

| **Keterangan** | **Data** |
|---|---|
| **Nama** | Fikri Yustiawan |
| **NIM** | 2225250075 |
| **Kelas** | 3-E |
| **Jurusan** | Pendidikan Matematika |

## Kasus

Program memproses data nilai mahasiswa dan memiliki tiga fungsi: `hitung_rata_rata`, `status`, dan `nilai_tertinggi`. Program berjalan tanpa `SyntaxError`, tetapi menghasilkan output yang salah. Versi awal ada di `kasus/kasus_04_praktik_awal.py`, versi perbaikan ada di `praktik/praktik_4_debugging.py`.

Output aktual awal (data `[80, 60, 90, 70]`):

```
Rata-rata: 60.0     (seharusnya 75.0)
Status 60: Tidak lulus   (seharusnya Lulus)
Tertinggi: 0        (seharusnya 90)
```

## Test Case

| ID | Target | Input | Expected | Actual Awal | Status Awal |
|---|---|---|---|---|---|
| T1 | rata-rata | `[80, 60, 90, 70]` | 75.0 | 60.0 | FAIL |
| T2 | rata-rata | `[100, 80]` | 90.0 | 36.0 | FAIL |
| T3 | status | `60` | Lulus | Tidak lulus | FAIL |
| T4 | status | `59` | Tidak lulus | Tidak lulus | PASS |
| T5 | tertinggi | `[80, 60, 90, 70]` | 90 | 0 | FAIL |
| T6 | rata-rata (kosong) | `[]` | 0 | 0.0 | PASS (kebetulan) |
| T7 | tertinggi (kosong) | `[]` | None | 0 | FAIL |
| T8 | tertinggi (negatif) | `[-5, -2, -9]` | -2 | -9 | FAIL |

T1-T5 adalah test case minimum dari modul. T6-T8 saya tambahkan untuk data kosong dan data negatif.

## Bug Report

| Bug ID | Gejala | Test | Lokasi | Akar Penyebab | Perbaikan | Retest |
|---|---|---|---|---|---|---|
| B01 | Rata-rata `[80, 60, 90, 70]` bernilai 60.0, bukan 75.0 | T1, T2 | `hitung_rata_rata`, `return sum(nilai) / 5` | Pembagi ditulis tetap 5, sehingga hanya benar jika datanya tepat 5. Data berisi 4 nilai tetap dibagi 5. | Pembagi diganti `len(nilai)`, ditambah penanganan list kosong agar tidak terjadi `ZeroDivisionError` | PASS |
| B02 | Nilai 60 dianggap "Tidak lulus" | T3 | `status`, `if nilai > 60` | Operator `>` mengecualikan nilai tepat di batas. Syarat kelulusan adalah nilai >= 60. | `>` diganti `>=` | PASS |
| B03 | Nilai tertinggi selalu 0 (atau malah nilai terkecil) | T5, T8 | `nilai_tertinggi`, `if x < tertinggi` | Operator pembanding terbalik: kode mencari nilai yang lebih kecil, bukan lebih besar. | `<` diganti `>` | PASS |
| B04 | Hasil 0 untuk list kosong dan list berisi nilai negatif | T7, T8 | `nilai_tertinggi`, `tertinggi = 0` | Nilai awal 0 bukan anggota data, sehingga data negatif tidak pernah bisa menang dan list kosong menghasilkan angka yang menyesatkan. | Nilai awal diambil dari `nilai[0]`, perulangan dimulai dari `nilai[1:]`, list kosong mengembalikan `None` | PASS |

Bukti investigasi: tracing manual pada `nilai_tertinggi([80, 60, 90, 70])` memperlihatkan variabel `tertinggi` tetap 0 pada setiap iterasi karena kondisi `x < 0` tidak pernah benar untuk nilai positif.

## Retest

Setelah perbaikan, seluruh test case dijalankan ulang:

| ID | Input | Expected | Actual | Status |
|---|---|---|---|---|
| T1 | `[80, 60, 90, 70]` | 75.0 | 75.0 | PASS |
| T2 | `[100, 80]` | 90.0 | 90.0 | PASS |
| T3 | `60` | Lulus | Lulus | PASS |
| T4 | `59` | Tidak lulus | Tidak lulus | PASS |
| T5 | `[80, 60, 90, 70]` | 90 | 90 | PASS |
| T6 | `[]` | 0 | 0 | PASS |
| T7 | `[]` | None | None | PASS |
| T8 | `[-5, -2, -9]` | -2 | -2 | PASS |

Ringkasan: 8/8 PASS. T4 yang sebelumnya PASS tetap PASS, jadi tidak ada regresi.

## Cara Menjalankan

```
python3 praktik/praktik_4_debugging.py
python3 praktik/uji_praktik_4.py
```

## Struktur Folder

```
pertemuan-13-debugging-2225250075/
|-- README.md
|-- .gitignore
|-- kasus/       (kasus_01 s.d. kasus_04, program bermasalah)
|-- latihan/     (01 s.d. 04, tracing dan test case)
|-- praktik/     (praktik_4_debugging.py dan uji_praktik_4.py)
`-- kuis/        (kuis formatif dalam bentuk PDF)
```

## Refleksi

Teknik debugging yang paling membantu adalah menulis test case terlebih dahulu, terutama test case batas. Bug `>` pada nilai 60 tidak terlihat jika hanya diuji dengan nilai 75, tetapi langsung ketahuan saat input 60 dibandingkan antara expected dan actual. Tracing manual juga membantu karena memperlihatkan bahwa variabel `tertinggi` tidak pernah berubah.

## Exit Ticket

- Teknik debugging yang paling membantu saya hari ini adalah membuat test case lalu membandingkan expected result dengan actual result, dibantu tracing nilai variabel.
- Bug logika lebih sulit daripada syntax error karena program tetap berjalan tanpa pesan error, sehingga kesalahan hanya bisa ditemukan dengan membandingkan hasil dengan yang seharusnya.
- Test case batas yang baik untuk program nilai adalah 59, 60, dan 61 (batas lulus), serta 0, 100, dan nilai di luar rentang seperti -1 atau 120.
- Kebiasaan debugging yang akan saya bawa ke proyek pertemuan 14 adalah menulis kriteria keberhasilan dan test case sejak awal, mengubah kode sesedikit mungkin, retest semua test setelah perbaikan, dan commit per perubahan.

## Sumber Bantuan

Saya menggunakan dokumentasi resmi Python dan VS Code, serta bantuan AI untuk menyusun struktur proyek dan dokumentasi. Test case, analisis bug, dan refleksi di atas sudah saya baca dan pahami.
