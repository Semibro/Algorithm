N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = arr[0][0]
delta = [(1, 0), (0, 1), (1, 1)]
for i in range(0, N):
    for j in range(0, M):
        if j < M-1 and i < N-1:
            if visited[i+1][j] <= arr[i+1][j] + visited[i][j]:
                visited[i+1][j] = arr[i+1][j] + visited[i][j]
            if visited[i][j+1] <= arr[i][j+1] + visited[i][j]:
                visited[i][j+1] = arr[i][j+1] + visited[i][j]
            if visited[i+1][j+1] <= arr[i+1][j+1] + visited[i][j]:
                visited[i+1][j+1] = arr[i+1][j+1] + visited[i][j]
        elif j == M-1 and i < N-1:
            if visited[i+1][j] <= arr[i+1][j] + visited[i][j]:
                visited[i+1][j] = arr[i+1][j] + visited[i][j]
        elif j < M-1 and i == N-1:
            if visited[i][j+1] <= arr[i][j+1] + visited[i][j]:
                visited[i][j+1] = arr[i][j+1] + visited[i][j]
print(visited[N-1][M-1])