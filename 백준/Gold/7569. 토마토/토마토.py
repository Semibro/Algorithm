from collections import deque

M, N, H = map(int, input().split())
tomato = []
queue = deque()

for z in range(H):
    tmp_lst = []
    for x in range(N):
        tmp_lst.append(list(map(int, input().split())))
        for y in range(M):
            if tmp_lst[x][y] == 1:
                queue.append((z, x, y))
    tomato.append(tmp_lst)

delta = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1)]

while queue:
    tz, tx, ty = queue.popleft()
    for d in delta:
        dz, dx, dy = tz+d[0], tx+d[1], ty+d[2]
        if 0<=dz<H and 0<=dx<N and 0<=dy<M and tomato[dz][dx][dy] == 0:
            tomato[dz][dx][dy] = tomato[tz][tx][ty] + 1
            queue.append((dz, dx, dy))

max_v = 1
for z in range(H):
    if max_v == 0:
        break
    for x in range(N):
        if max_v == 0:
            break
        for y in range(M):
            max_v = max(max_v, tomato[z][x][y])
            if tomato[z][x][y] == 0:
                max_v = 0
                break

if max_v == 0:
    print(-1)
elif max_v == 1:
    print(0)
else:
    print(max_v-1)