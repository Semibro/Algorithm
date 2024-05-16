import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chingho, power = [], []

for _ in range(N):
    x, y = input().split()
    chingho.append(x)
    power.append(int(y))

for _ in range(M):
    temp = int(input())
    s, e = 0, N
    while s <= e:
        m = (s + e) // 2
        if temp > power[m]:
            s = m + 1
        else:
            e = m - 1
    print(chingho[s])