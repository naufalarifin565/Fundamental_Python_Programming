def faktor_besar_ke_kecil(N):
    faktor = []
    for i in range(1, N + 1):
        if N % i == 0:
            faktor.append(i)
    faktor.sort(reverse=True)
    return faktor

# Membaca masukan dari pengguna
N = int(input("Masukkan bilangan bulat N: "))

# Mendapatkan faktor-faktor dan mengurutkannya
faktor_N = faktor_besar_ke_kecil(N)

# Menampilkan faktor-faktor
for faktor in faktor_N:
    print(faktor)
