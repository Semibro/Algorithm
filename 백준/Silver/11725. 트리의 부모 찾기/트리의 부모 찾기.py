## 접근방법
# 트리의 루트는 1이라고 정했으니까 1부터 DFS
# DFS끝에 도달했을 때 stack에서 pop하는 값을 따로 저장

import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

visited = [False] * (n+1)
stack = []
res = [0] * (n+1)

v = 1
visited[v] = True

while True:
    for w in graph[v]:
        if not visited[w]:
            stack.append(v)
            v = w
            visited[w] = True
            break
    else:
        if stack:
            s = stack.pop()
            res[v] = s
            v = s
        else:
            break

print(*res[2:], sep='\n')