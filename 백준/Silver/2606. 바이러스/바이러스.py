# input
import sys

node = int(sys.stdin.readline().rstrip())
line = int(sys.stdin.readline().rstrip())
adjM = [[0]*(node+1) for _ in range(node+1)]
for _ in range(line):
    u, v = map(int, input().split())
    adjM[u][v] = 1
    adjM[v][u] = 1

# dfs
visited = [False] * (node+1)
stack = []
res = []

v = 1
visited[v] = True
res.append(v)

while True:
    for w in range(node+1):
        if adjM[v][w] and not visited[w]:
            stack.append(v)
            v = w
            visited[w] = True
            res.append(w)
            break
    else:
        if stack:
            v = stack.pop()
        else:
            break

print(len(res)-1)