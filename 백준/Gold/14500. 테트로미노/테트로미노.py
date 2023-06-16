N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_v = 0

def bt(x, y, cnt, visit, res):
    global max_v
    if cnt == 4:
        max_v = max(max_v, res)
    else:
        for d in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            dx, dy = d[0]+x, d[1]+y
            if 0<=dx<N and 0<=dy<M and not visit[dx][dy]:
                visit[dx][dy] = True
                res += paper[dx][dy]
                bt(dx, dy, cnt+1, visit, res)
                res -= paper[dx][dy]
                visit[dx][dy] = False


def bt2(x, y):
    global max_v
    # ㅏ
    if 0<=x-1<N and 0<=x+1<N and 0<=y+1<M:
        max_v = max(max_v, paper[x][y]+paper[x-1][y]+paper[x+1][y]+paper[x][y+1])
    # ㅓ
    if 0<=x-1<N and 0<=x+1<N and 0<=y-1<M:
        max_v = max(max_v, paper[x][y]+paper[x-1][y]+paper[x+1][y]+paper[x][y-1])
    # ㅗ
    if 0<=x-1<N and 0<=y-1<M and 0<=y+1<M:
        max_v = max(max_v, paper[x][y]+paper[x-1][y]+paper[x][y-1]+paper[x][y+1])
    # ㅜ
    if 0<=x+1<N and 0<=y-1<M and 0<=y+1<M:
        max_v = max(max_v, paper[x][y]+paper[x+1][y]+paper[x][y-1]+paper[x][y+1])

for i in range(N):
    for j in range(M):
        bt2(i, j)
        visited[i][j] = True
        bt(i, j, 1, visited, paper[i][j])
        visited[i][j] = False

print(max_v)