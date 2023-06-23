import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    temp_lst = [(x, y)]
    sums = country[x][y]

    while queue:
        ix, iy = queue.popleft()
        for d in delta:
            dx, dy = ix + d[0], iy + d[1]
            if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy] and L <= abs(country[dx][dy] - country[ix][iy]) <= R:
                queue.append((dx, dy))
                visited[dx][dy] = 1
                temp_lst.append((dx, dy))
                sums += country[dx][dy]

    if len(temp_lst) > 1:
        for cx, cy in temp_lst:
            country[cx][cy] = sums // len(temp_lst)
        return 1
    return 0


while answer <= 2000:
    visited = [[0] * N for _ in range(N)]
    flag = 0

    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                flag = max(flag, bfs(x, y))

    if not flag:
        break
    answer += 1

print(answer)