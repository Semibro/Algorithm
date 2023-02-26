N = int(input())
changgo = []
for _ in range(N):
    a, b = map(int, input().split())
    changgo.extend([[a, b]])
maxV = max(changgo, key=lambda x:x[1])  # [8, 10]
maxL = max(changgo, key=lambda x:x[0])  # [15, 8]

lst = [0] * (maxL[0]+1)
for L, V in changgo:
    lst[L] = V
result = 0
tmp = 0
for i in range(0, maxV[0]):
    if lst[i] > tmp:
        tmp = lst[i]
    result += tmp
tmp2 = 0
for j in range(maxL[0], maxV[0]-1, -1):
    if lst[j] > tmp2:
        tmp2 = lst[j]
    result += tmp2

print(result)