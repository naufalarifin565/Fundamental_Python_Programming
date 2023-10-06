# Membaca input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# Mengecek apakah dua segmen garis bertabrakan
def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # Menentukan area dari empat titik
    def area(x1, y1, x2, y2, x3, y3):
        return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    
    # Menentukan apakah dua garis saling bersilangan
    def is_between(a, b, c):
        return min(a, b) <= c <= max(a, b)
    
    area1 = area(x1, y1, x2, y2, x3, y3)
    area2 = area(x1, y1, x2, y2, x4, y4)
    area3 = area(x3, y3, x4, y4, x1, y1)
    area4 = area(x3, y3, x4, y4, x2, y2)
    
    if (area1 * area2 < 0) and (area3 * area4 < 0):
        return True
    elif (area1 == 0 and is_between(x1, x2, x3) and is_between(y1, y2, y3)) or \
         (area2 == 0 and is_between(x1, x2, x4) and is_between(y1, y2, y4)) or \
         (area3 == 0 and is_between(x3, x4, x1) and is_between(y3, y4, y1)) or \
         (area4 == 0 and is_between(x3, x4, x2) and is_between(y3, y4, y2)):
        return True
    
    return False

# Menentukan output
if is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    print("awas nabrak")
else:
    print("gaspol bangg")
