from collections import deque

n = int(input())
house = [list(map(int, input())) for _ in range(n)]

queue = deque()
visited = [[False] * n for _ in range(n)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result = []

for i in range(n):
    for j in range(n):
        if house[i][j] == 1 and visited[i][j] == False:
            v = (i, j)
            queue.append(v)
            visited[i][j] = True
            cnt = 1
            while queue:
                t = queue.popleft()
                for d in delta:
                    w = [t[0]+d[0], t[1]+d[1]]
                    if 0 <= w[0] < n and 0 <= w[1] < n:
                        if house[w[0]][w[1]] == 1 and visited[w[0]][w[1]] == False:
                            visited[w[0]][w[1]] = True
                            cnt += 1
                            queue.append(w)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)
