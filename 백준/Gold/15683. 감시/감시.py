import copy

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 우 하 좌
direct = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
answer = 9876543210

# CCTV 개수 확인
CCTV = []
for i in range(N):
    for j in range(M):
        if 0 < room[i][j] < 6:
            CCTV.append([room[i][j], i, j])

# 방의 감시 상태 변경 함수
def watch(board, dir, x, y):
    for idx in dir:
        cx, cy = x, y
        while True:
            cx += delta[idx][0]
            cy += delta[idx][1]
            if 0 <= cx < N and 0 <= cy < M:
                if board[cx][cy] == 6:
                    break
                elif board[cx][cy] == 0:
                    board[cx][cy] = '#'
            else:
                break

# 백트래킹
def bfs(n, board):
    global answer
    if n == len(CCTV):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    cnt += 1
        answer = min(answer, cnt)
        return
    temp = copy.deepcopy(board)
    cctv_, x, y = CCTV[n]
    for k in direct[cctv_]:
        watch(temp, k, x, y)
        bfs(n+1, temp)
        temp = copy.deepcopy(board)

# 결과 출력
bfs(0, room)
print(answer)