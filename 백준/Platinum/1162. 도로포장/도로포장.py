import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
INF = float("inf")

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [[INF] * (K + 1) for _ in range(N + 1)]
heap = []

dist[1][0] = 0
heapq.heappush(heap, (0, 1, 0))

while heap:
    current_time, current_node, k_used = heapq.heappop(heap)

    if current_time > dist[current_node][k_used]:
        continue

    for next_node, cost in graph[current_node]:
        next_time = current_time + cost

        if next_time < dist[next_node][k_used]:
            dist[next_node][k_used] = next_time
            heapq.heappush(heap, (next_time, next_node, k_used))

        if k_used < K:
            paved_time = current_time + 0

            if paved_time < dist[next_node][k_used + 1]:
                dist[next_node][k_used + 1] = paved_time
                heapq.heappush(heap, (paved_time, next_node, k_used + 1))

print(min(dist[N]))