from heapq import heappush, heappop

# INPUT
N, M = map(int, input().split())
Farm = [[] for _ in range(N+1)]

# INPUT (무방향 그래프 생성)
for _ in range(M):
    A, B, C = map(int, input().split())
    Farm[A].append((B, C))
    Farm[B].append((A, C))

# INF값을 초기값으로 설정한 배열 생성
distance = [9876543210] * (N+1)

# heapq 사용을 위한 배열 생성
heap = []
distance[1] = 0  # 시작위치는 0
heappush(heap, (0, 1))  # 시작위치는 heapq에 넣는다.

# heap이 끝날 때까지 그래프를 확인하면서 최단거리 파악
while heap:
    dist, current = heappop(heap)
    if distance[current] >= dist:
        for next in Farm[current]:
            temp_dist = dist + next[1]
            if temp_dist < distance[next[0]]:
                distance[next[0]] = temp_dist
                heappush(heap, (temp_dist, next[0]))

print(distance[N])