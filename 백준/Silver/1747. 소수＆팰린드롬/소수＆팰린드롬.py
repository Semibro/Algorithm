def sosu(N):
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

def palin(N):
    check = str(N)
    for i in range(len(check)//2):
        if check[i] != check[-i-1]:
            return False
    return True

n = int(input())
for i in range(n, 2000002):
    if sosu(i) and palin(i):
        if i == 1:
            print(2)
            break
        else:
            print(i)
            break