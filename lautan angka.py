n = int(input())
s = input()
s_split = s.split(" ")
angka = 0

for i in range(n):
    angka += int(s_split[i])

bin_angka = str(bin(angka))

x = bin_angka.count("1")

print(x)