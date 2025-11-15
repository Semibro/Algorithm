import sys
import heapq

input = sys.stdin.readline

N, M, A, B, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]

max_edge_cost = 0
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    max_edge_cost = max(max_edge_cost, w)

INF = float('inf')

def check(max_allowed_shame):
    dist = [INF] * (N + 1)
    dist[A] = 0
    heap = []
    heapq.heappush(heap, (0, A))

    while heap:
        current_total_cost, current_node = heapq.heappop(heap)

        if current_total_cost > dist[current_node]:
            continue

        for next_node, cost in graph[current_node]:
            if cost > max_allowed_shame:
                continue

            new_total_cost = current_total_cost + cost

            if new_total_cost < dist[next_node]:
                dist[next_node] = new_total_cost
                heapq.heappush(heap, (new_total_cost, next_node))

    return dist[B] <= C

low = 0
high = max_edge_cost
answer = INF

while low <= high:
    mid = (low + high) // 2

    if check(mid):
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

if answer == INF:
    print(-1)
else:
    print(answer)