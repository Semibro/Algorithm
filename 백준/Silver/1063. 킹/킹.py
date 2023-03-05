board = [[-1] + [0]*8 + [-1] for _ in range(8)]
pad = [[-1] * 10]
chess = pad + board + pad
king, dol, N = input().split()
row = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
col = {'8': 1, '7': 2, '6': 3, '5': 4, '4': 5, '3': 6, '2': 7, '1': 8}
delta = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0), 'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}
k = []
d = []
k.append(col.get(king[1])); k.append(row.get(king[0])); d.append(col.get(dol[1])); d.append(row.get(dol[0]))
for _ in range(int(N)):
    dist = input()
    a = delta.get(dist)
    n = (k[0]+a[0], k[1]+a[1])
    if chess[n[0]][n[1]] == -1:
        pass
    else:
        if n[0] == d[0] and n[1] == d[1]:
            if chess[d[0]+a[0]][d[1]+a[1]] == -1:
                pass
            else:
                d[0] += a[0]
                d[1] += a[1]
                k[0] = n[0]
                k[1] = n[1]
        else:
            k[0] = n[0]
            k[1] = n[1]
res_k = ''
res_d = ''
for k1, v1 in row.items():
    if v1 == k[1]:
        res_k += k1
    if v1 == d[1]:
        res_d += k1
for k2, v2 in col.items():
    if v2 == k[0]:
        res_k += k2
    if v2 == d[0]:
        res_d += k2
print(res_k)
print(res_d)