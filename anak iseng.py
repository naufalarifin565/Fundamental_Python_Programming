char_swap = input()

n = int(input())

# Membaca dan memproses setiap string yang akan dipulihkan
restored_strings = []
for _ in range(n):
    s = input()
    restored_s = ''.join([char_swap[ord(c) - ord('a')] if 'a' <= c <= 'z' else c for c in s])
    restored_strings.append(restored_s)

for restored_s in restored_strings:
    print(restored_s)
