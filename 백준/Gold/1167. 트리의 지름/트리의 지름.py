# recursion error 방지
import sys
sys.setrecursionlimit(10**9)

# 정점의 개수
V = int(input())

# 트리 그래프
graph = [[] for _ in range(V+1)]

# 트리 정보
for _ in range(V):
    tree_info = list(map(int, input().split()))
    for i in range(1, len(tree_info)-1, 2):
        graph[tree_info[0]].append([tree_info[i], tree_info[i+1]])

# DFS
def dfs(C, W):
    for i in graph[C]:
        a, b = i
        if distance[a] == -1:
            distance[a] = W + b
            dfs(a, W+b)

# 시작지점 찾기
distance = [-1] * (V+1)
distance[1] = 0
dfs(1, 0)
start = distance.index(max(distance))

# 가장 먼 곳 찾기
distance = [-1] * (V+1)
distance[start] = 0
dfs(start, 0)

# 결과 출력
print(max(distance))