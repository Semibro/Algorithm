from collections import deque

def solution(board):
    answer = -1
    n, m = len(board), len(board[0])
    pad = ['D' * (m+2)]
    for i in range(n):
        board[i] = 'D' + board[i] + 'D'
    board = pad + board + pad
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] == 'R':
                start = [i, j]
                break
    
    visited = [[0]*(m+2) for _ in range(n+2)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    while queue:
        tx, ty = queue.popleft()
        for d in delta:
            for j in range(1, 101):
                dx, dy = tx+d[0]*j, ty+d[1]*j
                if 0 <= dx < n+2 and 0 <= dy < m+2:
                    if board[dx][dy] == 'D':
                        nx, ny = tx+d[0]*(j-1), ty+d[1]*(j-1)
                        if not visited[nx][ny]:
                            visited[nx][ny] = visited[tx][ty] + 1
                            if board[nx][ny] == 'G':
                                answer = visited[nx][ny]-1
                            else:
                                queue.append((nx, ny))
                        break
            
    return answer