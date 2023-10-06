n = int(input())

jadwal_mahasiswa = list(map(int, input().split()))

hari_terakhir = input()

hari_urutan = {
    "Minggu": 0,
    "Senin": 1,
    "Selasa": 2,
    "Rabu": 3,
    "Kamis": 4,
    "Jumat": 5,
    "Sabtu": 6,
}

total_hari = hari_urutan[hari_terakhir]
for h in jadwal_mahasiswa:
    total_hari = (total_hari - h) % 7

for nama_hari, urutan in hari_urutan.items():
    if urutan == total_hari:
        hari_terakhir = nama_hari
        break

print(hari_terakhir)