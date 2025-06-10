from collections import deque

def solution(land):
    N, M = len(land), len(land[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    oils = [0 for _ in range(M)]
    
    for j in range(M):
        for i in range(N):
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque()
                colums = set()
                
                queue.append((i, j))
                visited[i][j] = True
                oil_count = 1
                colums.add(j)
                
                while queue:
                    cx, cy = queue.popleft()
                    for d in direction:
                        nx, ny = cx + d[0], cy + d[1]
                        if 0 <= nx < N and 0 <= ny < M:
                            if land[nx][ny] == 1 and not visited[nx][ny]:
                                oil_count += 1
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                colums.add(ny)
                                
                for col in colums:
                    oils[col] += oil_count

    return max(oils)