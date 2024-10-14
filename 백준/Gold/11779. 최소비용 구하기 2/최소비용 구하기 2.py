import sys
import heapq

input = sys.stdin.readline
INF = 9876543210

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())
distance = [INF] * (n+1)
route = [0] * (n+1)

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                route[i[0]] = now
                heapq.heappush(queue, (cost, i[0]))

    return distance

dijkstra(start)

print(distance[end])

path = [end]
temp = end
while temp != start:
    path.append(route[temp])
    temp = route[temp]

route = path[::-1]
print(len(route))
print(*route)