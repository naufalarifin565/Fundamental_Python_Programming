MAX_N = 40


ways_to_build = [0] * (MAX_N + 1)


ways_to_build[0] = 1
ways_to_build[1] = 1


for n in range(2, MAX_N + 1):
    
    ways_to_build[n] = ways_to_build[n - 1] + ways_to_build[n - 2]


while True:
    n = int(input())
    if n == -1:
        break
    print(ways_to_build[2 * n])