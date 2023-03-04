import sys
input = sys.stdin.readline
M = int(input())
result = 0
xor = 0
for _ in range(M):
    a = list(map(int, input().split()))
    if a[0] == 1:
        result += a[1]
        xor = xor ^ a[1]
    elif a[0] == 2:
        result -= a[1]
        xor = xor ^ a[1]
    elif a[0] == 3:
        print(result)
    else:
        print(xor)