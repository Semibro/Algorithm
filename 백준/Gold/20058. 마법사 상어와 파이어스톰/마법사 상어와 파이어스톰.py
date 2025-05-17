from collections import deque

N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2 ** N)]
Ls = list(map(int, input().split()))
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def rotate(grid, L):
    N = len(grid)
    new_grid = [[0] * N for _ in range(N)]
    size = 2 ** L

    for x in range(0, N, size):
        for y in range(0, N, size):
            for i in range(size):
                for j in range(size):
                    new_grid[x + j][y + size - 1 - i] = grid[x + i][y + j]
    
    return new_grid

def melt_ice(grid):
    N = len(grid)
    new_grid = [row[:] for row in grid]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                continue

            cnt = 0
            for dx, dy in direction:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] > 0:
                    cnt += 1
            
            if cnt < 3:
                new_grid[i][j] -= 1

    return new_grid

for L in Ls:
    A = rotate(A, L)
    A = melt_ice(A)

total_ice = 0
for idx in range(2 ** N):
    total_ice += sum(A[idx])

def bfs(grid):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    max_size_ice = 0

    for i in range(N):
        for j in range(N):
            if grid[i][j] > 0 and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                temp_size = 1

                while queue:
                    cx, cy = queue.popleft()
                    for dx, dy in direction:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] > 0:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            temp_size += 1

                max_size_ice = max(max_size_ice, temp_size)
    
    return max_size_ice

print(total_ice)
print(bfs(A))