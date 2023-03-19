N, L, D = map(int, input().split())
total = ((L+5)*N)-5
song = [False] * total
s = 1
for i in range(0, total, L+5):
    for j in range(i, i+L):
        song[j] = True
for i in range(D, total, D):
    if song[i] == False:
        print(i)
        break
else:
    while D * s < total:
        s += 1
    print(D * s)