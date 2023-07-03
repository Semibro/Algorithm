import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, W = map(int, input().split())
    graph[A].append((W, B))

def dijkstra(n):
    dp = [9876543210] * (N+1)
    dp[n], dp[0] = 0, 0
    heap = []
    heappush(heap, (0, n))
    while heap:
        weight, idx = heappop(heap)
        if dp[idx] < weight:
            continue
        for wgh, next_idx in graph[idx]:
            next_wgh = weight + wgh
            if next_wgh < dp[next_idx]:
                dp[next_idx] = next_wgh
                heappush(heap, (next_wgh, next_idx))
    return dp

answer = dijkstra(X)
for i in range(1, N+1):
    if i != X:
        result = dijkstra(i)
        answer[i] += result[X]

print(max(answer))