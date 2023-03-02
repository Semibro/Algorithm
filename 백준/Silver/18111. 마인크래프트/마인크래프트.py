import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
mine = [list(map(int, input().split())) for _ in range(N)]
counts = [0] * 257
for i in range(N):
    for j in range(M):
        counts[mine[i][j]] += 1
t = 0
for i in range(len(counts)):
    if counts[i] > 0:
        min_Idx = i
        break
for i in range(len(counts)-1, -1, -1):
    if counts[i] > 0:
        max_Idx = i
        break
while min_Idx != max_Idx:
    if B >= counts[min_Idx]:
        if counts[min_Idx] <= 2 * counts[max_Idx]:
            B -= counts[min_Idx]
            t += counts[min_Idx]
            counts[min_Idx+1] += counts[min_Idx]
            counts[min_Idx] = 0
            min_Idx += 1
        else:
            B += counts[max_Idx]
            t += 2 * counts[max_Idx]
            counts[max_Idx - 1] += counts[max_Idx]
            counts[max_Idx] = 0
            max_Idx -= 1
    else:
        B += counts[max_Idx]
        t += 2 * counts[max_Idx]
        counts[max_Idx - 1] += counts[max_Idx]
        counts[max_Idx] = 0
        max_Idx -= 1

print(f'{t} {counts.index(max(counts))}')