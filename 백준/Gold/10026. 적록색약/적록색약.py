from collections import deque
import copy

N = int(input())
color = [list(input()) for _ in range(N)]
color_p = copy.deepcopy(color)

for i in range(N):
    for j in range(N):
        if color_p[i][j] == 'G':
            color_p[i][j] = 'R'


def bfs(lst):
    queue = deque()
    visited = [[False]*N for _ in range(N)]
    count = 0
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                c = lst[x][y]
                queue.append((x, y))
                visited[x][y] = True
                count += 1
                while queue:
                    tx, ty = queue.popleft()
                    for d in delta:
                        dx, dy = tx+d[0], ty+d[1]
                        if 0<=dx<N and 0<=dy<N:
                            if not visited[dx][dy] and lst[dx][dy] == c:
                                visited[dx][dy] = True
                                queue.append((dx, dy))

    return count

print(bfs(color), bfs(color_p))