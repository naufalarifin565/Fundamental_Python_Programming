
T = int(input())

def cetakA(N, M):
    print(f'Pattern no : {pattern_no}')
    
    for i in range(N):
        if (i+1) % 2==1:
            print(' ',end="")
        for j in range(M):
            if j % 2 == 0:
                print('.',end="")
            else:
                print('-', end="")
        print()
def cetakB(N, M):
    print(f'Pattern no : {pattern_no}')
    
    for i in range(N):
        if (i+1) % 2==0:
            print(' ',end="")
        for j in range(M):
            if j % 2 == 0:
                print('-',end="")
            else:
                print('.', end="")
        print()


for pattern_no in range(1, T + 1):
    pattern_type, N, M = input().split()
    N, M = int(N), int(M)
    if pattern_type=='A':
        cetakA(N, M)
    else:
        cetakB(N, M)
    
