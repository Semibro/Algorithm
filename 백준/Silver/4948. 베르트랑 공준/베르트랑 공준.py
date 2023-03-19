def sosu(N):
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

while True:
    x = int(input())
    if x == 0:
        break
    else:
        count = 0
        for i in range(x+1, 2*x+1):
            if sosu(i):
                count += 1
        print(count)