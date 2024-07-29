import sys
from collections import deque

input = sys.stdin.readline

# F: 최고층  /  S: 강호위치  /  G: 도착위치  /  U: 위로U만큼  /  D: 아래로D만큼
F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)

def bfs():
    queue = deque()
    queue.append(S)

    visited[S] = 1

    while queue:
        temp = queue.popleft()
        if temp == G:
            return visited[temp] - 1
        else:
            for i in (temp-D, temp+U):
                if (0 < i <= F) and visited[i] == 0:
                    visited[i] = visited[temp] + 1
                    queue.append(i)
    
    return "use the stairs"

print(bfs())