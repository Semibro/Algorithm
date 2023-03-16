def sosu(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    a, b = N//2, N//2
    while a != 0:
        if sosu(a) and sosu(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1