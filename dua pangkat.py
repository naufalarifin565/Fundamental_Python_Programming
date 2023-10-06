n = int(input())
flag = 0
while(n > 1):
    if(n%2 == 0):
        n /= 2
        continue
    else:
        flag = 1
        break
if not flag:
    print("ya")
else:
    print("bukan")
