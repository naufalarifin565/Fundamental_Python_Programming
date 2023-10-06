
# Fungsi untuk menghitung kuadran dari sebuah titik
def hitung_kuadran(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0  # Pusat koordinat

# Fungsi untuk menentukan apakah sebuah titik berada di antara dua titik lainnya
def segaris(x1, y1, x2, y2, x, y):
    return (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1)

# Membaca koordinat dari input
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Px, Py = map(int, input().split())

# Menghitung kuadran dari titik-titik pengawas
kuadran_A = hitung_kuadran(Ax, Ay)
kuadran_B = hitung_kuadran(Bx, By)
kuadran_C = hitung_kuadran(Cx, Cy)

# Menampilkan kuadran dari titik-titik pengawas
print(f"TITIK PENGAWAS: kuadran {kuadran_A} {kuadran_B} {kuadran_C}")

# Memeriksa apakah Bjarkan berada di dalam segitiga atau di luar segitiga
if segaris(Ax, Ay, Bx, By, Px, Py) or segaris(Bx, By, Cx, Cy, Px, Py) or segaris(Cx, Cy, Ax, Ay, Px, Py):
    print("KEPUNG BJARKAN!!!, Dia Segaris Dengan Kalian")
else:
    print("Yo Ndak Tau Kok Tanya Saya")