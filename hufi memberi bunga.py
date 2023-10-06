def favorit_mehas(num):
    if num % 2 == 0:
        return True
    else:
        return False

n = int(input())

for _ in range(n):
    x = int(input())
    
    if favorit_mehas(x):
        print("Mehas pasti suka")
    else:
        print("jangan ini, deh")