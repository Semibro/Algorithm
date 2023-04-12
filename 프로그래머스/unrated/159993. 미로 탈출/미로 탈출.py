from collections import deque

def solution(maps):
    # 기본 셋팅 (패딩)
    n, m = len(maps), len(maps[0])
    pad = ["X" * (m+2)]
    for i in range(n):
        maps[i] = "X" + maps[i] + "X"
    maps = pad + maps + pad
    answer = 0
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # 시작점, 레버, 도착점 찾기
    for i in range(1, n+1):
        for j in range(1, m+1):
            if maps[i][j] == "S":
                start = [i, j]
            if maps[i][j] == "E":
                end = [i, j]
            if maps[i][j] == "L":
                lever = [i, j]
    
    # 레버까지의 거리 찾기
    queue = deque()
    visited = [[0] * (m+2) for _ in range(n+2)]
    visited[start[0]][start[1]] = 1
    queue.append(start)
    while queue:
        if answer > 0:
            break
        tx, ty = queue.popleft()
        for d in delta:
            dx, dy = tx+d[0], ty+d[1]
            if maps[dx][dy] != 'X' and not visited[dx][dy]:
                queue.append([dx, dy])
                visited[dx][dy] = visited[tx][ty] + 1
            if maps[dx][dy] == 'L':
                answer += visited[tx][ty]
    
    # 도착지까지 거리 찾기
    if answer == 0:
        return -1
    else:
        queue = deque()
        visited = [[0] * (m+2) for _ in range(n+2)]
        visited[lever[0]][lever[1]] = 1
        queue.append(lever)
        while queue:
            tx, ty = queue.popleft()
            for d in delta:
                dx, dy = tx+d[0], ty+d[1]
                if maps[dx][dy] != 'X' and not visited[dx][dy]:
                    queue.append([dx, dy])
                    visited[dx][dy] = visited[tx][ty] + 1
                if maps[dx][dy] == 'E':
                    answer += visited[tx][ty]
                    return answer
        else:
            return -1