from collections import deque

tc = int(input())

for _ in range(tc):
    I = int(input())
    knight_x, knight_y = map(int, input().split())
    move_x, move_y = map(int, input().split())
    
    chess = [[-1]*I for _ in range(I)]
    d = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    
    def bfs():
        queue = deque()
        queue.append((knight_x, knight_y))
        chess[knight_x][knight_y] += 1

        while queue:
            temp_x, temp_y = queue.popleft()

            if temp_x == move_x and temp_y == move_y:
                return chess[temp_x][temp_y]

            for dx, dy in d:
                nx, ny = temp_x + dx, temp_y + dy

                if 0<=nx<I and 0<=ny<I:
                    if chess[nx][ny] == -1:
                        queue.append((nx, ny))
                        chess[nx][ny] = chess[temp_x][temp_y] + 1

    print(bfs())