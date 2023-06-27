import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
# 플로이드-워셜을 사용하기 위해 max cost값 설정 (비용은 100,000보다 작거나 같은 자연수 이므로 100,001 설정)
graph = [[9876543210 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    # 더 적은 비용으로 갈 수 있도록 cost랑 현재값을 비교
    graph[start][end] = min(cost, graph[start][end])

# 플로이드-워셜
for k in range(n+1):
    for x in range(n+1):
        for y in range(n+1):
            if x == y:
                graph[x][y] = 0
            else:  # 플로이드-워셜 핵심 : 직접가는 비용과 k를 거쳐가는 비용을 비교해 더 작은 방법으로 선택
                graph[x][y] = min(graph[x][y], graph[x][k]+graph[k][y])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 9876543210:
            graph[i][j] = 0

for idx in range(1, n+1):
    print(*graph[idx][1:])