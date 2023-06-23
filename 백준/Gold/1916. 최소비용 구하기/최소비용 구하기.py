import sys
input = sys.stdin.readline
from heapq import heappush, heappop  # 다익스트라 알고리즘은 heapq 사용하기!

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
dp = [9876543210] * (N+1)
heap = []
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
start, end = map(int, input().split())

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

dijkstra(start)
print(dp[end])