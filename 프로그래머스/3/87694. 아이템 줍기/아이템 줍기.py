from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    SIZE = 102
    board = [[0] * SIZE for _ in range(SIZE)]

    # 1. 좌표 2배 확장해서 사각형 채우기
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[y][x] = 1

    # 2. 내부 비우기 (1로 채운 후 진짜 내부를 -1로)
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[y][x] = -1

    # 3. BFS 탐색
    visited = [[0] * SIZE for _ in range(SIZE)]
    q = deque()
    sx, sy = characterX * 2, characterY * 2
    ex, ey = itemX * 2, itemY * 2
    q.append((sy, sx))
    visited[sy][sx] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        y, x = q.popleft()
        if x == ex and y == ey:
            return (visited[y][x] - 1) // 2  # 2배 좌표였으므로 절반

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if board[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))