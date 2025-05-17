# input
N, M, K = map(int, input().split())
# fire_ball = [r, c, m, s, d]
# i번 파이어볼의 위치: (r, c), 질량: m, 속력: s, 방향: d
fire_ball = [list(map(int, input().split())) for _ in range(M)]
board = [[[] for _ in range(N)] for _ in range(N)]
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for k in range(K):
    for r, c, m, s, d in fire_ball:
        arrived_x, arrived_y = (r + (direction[d][0] * s)) % N, (c + (direction[d][1] * s)) % N
        board[arrived_x][arrived_y].append((m, s, d))

    fire_ball = []

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                new_m, new_s = 0, 0
                even_count, odd_count = 0, 0
                for m, s, d in board[i][j]:
                    new_m += m
                    new_s += s
                    if d % 2 == 0:
                        even_count += 1
                    else:
                        odd_count += 1
                
                new_m = new_m // 5
                if new_m == 0:
                    board[i][j] = []
                    continue
                new_s = new_s // len(board[i][j])
                if even_count > 0 and odd_count > 0:
                    board[i][j] = [(new_m, new_s, 1), (new_m, new_s, 3), (new_m, new_s, 5), (new_m, new_s, 7)]
                    fire_ball.append((i, j, new_m, new_s, 1))
                    fire_ball.append((i, j, new_m, new_s, 3))
                    fire_ball.append((i, j, new_m, new_s, 5))
                    fire_ball.append((i, j, new_m, new_s, 7))
                else:
                    board[i][j] = [(new_m, new_s, 0), (new_m, new_s, 2), (new_m, new_s, 4), (new_m, new_s, 6)]
                    fire_ball.append((i, j, new_m, new_s, 0))
                    fire_ball.append((i, j, new_m, new_s, 2))
                    fire_ball.append((i, j, new_m, new_s, 4))
                    fire_ball.append((i, j, new_m, new_s, 6))
            elif len(board[i][j]) == 1:
                m, s, d = board[i][j][0]
                fire_ball.append((i, j, m, s, d))

    if k < K - 1:
        board = [[[] for _ in range(N)] for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(N):
        if len(board[i][j]) > 0:
            for m, s, d in board[i][j]:
                answer += m

print(answer)