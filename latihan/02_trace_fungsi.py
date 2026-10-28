"""Latihan 2 - Menelusuri fungsi.
Pasang breakpoint di baris print, lalu Step Into ke hitung_diskon.
Variables: total=200000, persen=10 -> diskon=20000.0 -> return 180000.0
"""


def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon


print(hitung_diskon(200000, 10))
