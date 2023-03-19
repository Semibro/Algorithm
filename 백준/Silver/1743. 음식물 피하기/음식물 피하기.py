from collections import deque

N, M, K = map(int, input().split())
lst = [[-1] + [0] * M + [-1] for _ in range(N)]
pad = [[-1] * (M+2)]
arr = pad + lst + pad
for _ in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 1

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * (M+2) for _ in range(N+2)]
result = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == 1 and visited[i][j] == 0:
            count = 1
            queue = deque()
            visited[i][j] = 1
            queue.append((i, j))
            while queue:
                t = queue.popleft()
                for d in delta:
                    si, sj = t[0] + d[0], t[1] + d[1]
                    if arr[si][sj] == 1 and visited[si][sj] == 0:
                        count += 1
                        visited[si][sj] = 1
                        arr[si][sj] = arr[t[0]][t[1]] + 1
                        queue.append((si, sj))
            result.append(count)

print(max(result))