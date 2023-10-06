exp_kurang = int(input())
#input = 127
abyss = 0
hilichurl = 0
slime = 0
if (exp_kurang % 2 == 1):
    exp_kurang += 1
sisa = exp_kurang % 10
if sisa == 0:
    abyss = exp_kurang // 10
elif sisa == 2:
    abyss = (exp_kurang // 10) - 1
    slime = 2
elif sisa == 4:
    abyss = (exp_kurang // 10) - 1
    hilichurl = 1
    slime = 1
elif sisa == 6:
    abyss = exp_kurang // 10
    slime = 1
elif sisa == 8:
    abyss = exp_kurang // 10
    hilichurl = 1
print((exp_kurang + 1) // 2)
print(slime)
print(hilichurl)
print(abyss)
