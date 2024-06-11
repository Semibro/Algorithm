from heapq import heappush, heappop

N, D = map(int, input().split())
gil = [i for i in range(D+1)]
jireumgil = []

for _ in range(N):
    jireumgil.append(list(map(int, input().split())))

for i in range(0, D+1):
    if i > 0:
        gil[i] = min(gil[i], gil[i-1]+1)

    for s, e, j in jireumgil:
        if i == s and e <= D and gil[i]+j < gil[e]:
            gil[e] = gil[i] + j

print(gil[D])