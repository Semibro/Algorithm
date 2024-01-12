from collections import deque

def solution(maps):
    answer = 0 # 정답출력을 위한 변수
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 방향
    n, m = len(maps), len(maps[0])
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        i, j = queue.popleft()
        for dx, dy in direction:
            nx, ny = dx+i, dy+j
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[i][j] + 1
                queue.append((nx, ny))
        
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
    
    return answer