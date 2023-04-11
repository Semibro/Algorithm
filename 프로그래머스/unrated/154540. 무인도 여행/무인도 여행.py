from collections import deque

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    
    pad = ["X"*(m+2)]
    for i in range(n):
        maps[i] = 'X'+maps[i]+'X'
    maps = pad + maps + pad
    
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[False]*(m+2) for _ in range(n+2)]
    
    queue = deque()
    for i in range(1, n+1):
        for j in range(1, m+1):
            if maps[i][j] != 'X':
                if not visited[i][j]:
                    res = int(maps[i][j])
                    queue.append((i, j))
                    visited[i][j] = True
                    while queue:
                        tx, ty = queue.popleft()
                        for d in delta:
                            dx, dy = tx+d[0], ty+d[1]
                            if maps[dx][dy] != 'X' and not visited[dx][dy]:
                                queue.append((dx, dy))
                                visited[dx][dy] = True
                                res += int(maps[dx][dy])
                    answer.append(res)
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]