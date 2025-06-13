from collections import deque

def bfs(p):
    for i in range(5):
        for j in range(5):
            if p[i][j] == "P":
                queue = deque()
                visited = [[False for _ in range(5)] for _ in range(5)]
                direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

                queue.append((i, j, 0))
                visited[i][j] = True

                while queue:
                    cx, cy, dist = queue.popleft()
                    for dx, dy in direction:
                        nx, ny = cx + dx, cy + dy

                        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                            visited[nx][ny] = True

                            if p[nx][ny] == "X":
                                continue
                            if p[nx][ny] == "P":
                                return 0
                            if p[nx][ny] == "O" and dist < 1:
                                queue.append((nx, ny, dist+1))

    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(bfs(place))
        
    return answer