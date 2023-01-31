rows = 100
cols = 100
white = [[0 for j in range(cols)] for i in range(rows)]
rlt = 0

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            white[y-1+j][x-1+k] = 1
for m in white:
    rlt += m.count(1)

print(rlt)