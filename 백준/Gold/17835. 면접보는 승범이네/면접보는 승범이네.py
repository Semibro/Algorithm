import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
INF = float('inf')

for _ in range(M):
    U, V, C = map(int, input().split())
    graph[V].append((U, C))

cities = list(map(int, input().split()))

heap = []
dist = [INF] * (N + 1)

for city in cities:
    dist[city] = 0
    heapq.heappush(heap, (0, city))

while heap:
    cd, cn = heapq.heappop(heap)

    if dist[cn] < cd:
        continue

    for nn, c in graph[cn]:
        nd = cd + c

        if nd < dist[nn]:
            dist[nn] = nd
            heapq.heappush(heap, (nd, nn))

max_value = -1
max_idx = -1

for idx in range(1, N + 1):
    if dist[idx] == INF:
        continue

    if dist[idx] > max_value:
        max_value = dist[idx]
        max_idx = idx

print(max_idx)
print(max_value)