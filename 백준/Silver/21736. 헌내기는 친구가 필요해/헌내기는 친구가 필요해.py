from collections import deque

N, M = map(int, input().split())
board = [['X'] + list(input()) + ['X'] for _ in range(N)]
pad = [['X'] * (M+2)]
campus = pad + board + pad

for i in range(1, N+1):
    for j in range(1, M+1):
        if campus[i][j] == 'I':
            start = (i, j)
            break

cnt = 0
visited = [[False] * (M+2) for _ in range(N+2)]
v = start
queue = deque()
queue.append(v)
visited[v[0]][v[1]] = True
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while queue:
    t = queue.popleft()
    for d in delta:
        w = [t[0] + d[0], t[1] + d[1]]
        if campus[w[0]][w[1]] == 'P' and not visited[w[0]][w[1]]:
            visited[w[0]][w[1]] = True
            queue.append(w)
            cnt += 1

        if campus[w[0]][w[1]] == 'O' and not visited[w[0]][w[1]]:
            visited[w[0]][w[1]] = True
            queue.append(w)

        # if campus[w[0]][w[1]] == 'X':
        #     break
if cnt == 0:
    print('TT')
else:
    print(cnt)