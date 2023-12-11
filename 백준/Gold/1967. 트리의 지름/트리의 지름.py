# 제출하면 recursion error 발생.
# 따라서 recursion error를 잡기위해 sys를 사용해 제한을 걸어야 한다.
import sys
sys.setrecursionlimit(10**9)

n = int(input())

# 트리 그래프
# 트리의 노드가 1부터 시작인 것을 생각하여 n보다 1크게
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent_node, children_node, weight = map(int, input().split())
    graph[parent_node].append([children_node, weight])
    graph[children_node].append([parent_node, weight])

# DFS를 통해 가장 먼 노드를 구하는데 사용.
# graph를 돌면서 방문한 적이 없는 곳(-1)이면 방문 처리를 하고 가중치를 표시.
def dfs(c, w):
    for i in graph[c]:
        a, b = i
        if distance[a] == -1:
            distance[a] = w + b
            dfs(a, w + b)

# DFS 방문을 위한 리스트 생성
# 트리의 지름을 구하는 방법
# 루트노드(임의의 노드)에서 가장 먼 곳을 체크한다.
# 체크 된 곳에서 가장 먼 곳을 찾는다.
distance = [-1] * (n+1)
# 루트노드
distance[1] = 0
# DFS 동작
dfs(1, 0)

# 시작 지점 체크
start = distance.index(max(distance))

# 시작지점에서 가장 먼 곳을 찾는다.
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

# 결과 출력
print(max(distance))