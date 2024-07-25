from collections import deque

n, m = map(int, input().split())
count, answer = 0, 0

dohwaji = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    for j in range(m):
        if dohwaji[i][j] == 1 and not visited[i][j]:
            count += 1
            temp = 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True

            while queue:
                tx, ty = queue.popleft()
                for x, y in d:
                    dx, dy = tx+x, ty+y
                    if 0<=dx<n and 0<=dy<m and dohwaji[dx][dy] == 1 and not visited[dx][dy]:
                        temp += 1
                        queue.append((dx, dy))
                        visited[dx][dy] = True

            answer = max(answer, temp)

if count > 0:
    print(count)
    print(answer)
else:
    print(0)
    print(0)