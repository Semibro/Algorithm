from collections import deque

def bfs(tx, ty):
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    queue.append((tx, ty))
    visited[tx][ty] = 1
    t_list, dist = [], -1
    
    while queue:
        cx, cy = queue.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = cx + di, cy + dj
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and baby_shark >= space[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
                if baby_shark > space[nx][ny] > 0:
                    if dist == -1 or visited[nx][ny] == dist:
                        t_list.append((nx, ny))
                        dist = visited[nx][ny]
                    elif visited[nx][ny] < dist:
                        t_list = [(nx, ny)]
                        dist = visited[nx][ny]

    return t_list, dist - 1

###

N = int(input())
# 0: 빈칸 / 1~6: 물고기 크기 / 9: 아기 상어(처음크기 2)
space = [list(map(int, input().split())) for _ in range(N)]  # 공간

# 기본값 세팅
baby_shark, eat, answer = 2, 0, 0
# 아기상어 위치 찾기
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_x, shark_y = i, j
            space[i][j] = 0
            break

while True:
    temp_list, distance = bfs(shark_x, shark_y)

    if len(temp_list) == 0:
        break

    temp_list.sort(key=lambda x: (x[0], x[1]))
    shark_x, shark_y = temp_list[0]  # 아기상어 위치 초기화
    space[shark_x][shark_y] = 0
    answer += distance
    eat += 1

    if baby_shark == eat:
        baby_shark += 1
        eat = 0

print(answer)
