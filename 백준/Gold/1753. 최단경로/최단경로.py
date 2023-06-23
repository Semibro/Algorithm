import sys
input = sys.stdin.readline
from heapq import heappush, heappop  # 다익스트라 알고리즘은 heapq 사용하기!

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
dp = [9876543210] * (V+1)
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def dijkstra(n):
    dp[n] = 0
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

dijkstra(K)
for i in range(1, V+1):
    if dp[i] == 9876543210:
        print('INF')
    else:
        print(dp[i])