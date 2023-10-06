def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix[0]
        matrix = list(zip(*matrix[1:]))[::-1]
    return result

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

spiral_result = spiral_order(matrix)

print(*spiral_result)