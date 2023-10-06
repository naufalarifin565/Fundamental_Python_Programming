# Membaca input N dan K
N, K = map(int, input().split())

# Loop untuk mencetak deret bilangan dari 1 hingga N
for i in range(1, N + 1):
    # Cek apakah bilangan harus diganti dengan tanda bintang
    if i % K == 0:
        print('*', end=' ')
    else:
        print(i, end=' ')

    # Pindah ke baris berikutnya setelah mencetak 11 bilangan
    if i % 11 == 0:
        print()
