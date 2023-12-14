# 집의 크기 NXN
N = int(input())
# 집의 상태 (벽으로 둘러쌓아서 밖으로 나가지 못하게 변경)
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

# 정답 출력을 위한 count 변수 생성
count = 0

# DFS 함수
def dfs(direction):
    global count
    x, y, z = direction

    # (N, N) 도착
    if x == N-1 and y == N-1:
        count += 1
        return

    # 전의 파이프가 가로일 경우
    if z == 0:
        # 가로이동
        if y+1 < N and house[x][y+1] == 0:
            dfs((x, y+1, 0))
        # 대각선이동
        if x+1 < N and y+1 < N and house[x+1][y+1] == 0 and house[x][y+1] == 0 and house[x+1][y] == 0:
            dfs((x+1, y+1, 2))

    # 전의 파이프가 세로일 경우
    if z == 1:
        # 세로이동
        if x+1 < N and house[x+1][y] == 0:
            dfs((x+1, y, 1))
        # 대각선이동
        if x+1 < N and y+1 < N and house[x+1][y+1] == 0 and house[x][y+1] == 0 and house[x+1][y] == 0:
            dfs((x+1, y+1, 2))

    # 전의 파이프가 대각선일 경우
    if z == 2:
        # 가로이동
        if y+1 < N and house[x][y+1] == 0:
            dfs((x, y+1, 0))
        # 세로이동
        if x+1 < N and house[x+1][y] == 0:
            dfs((x+1, y, 1))
        # 대각선이동
        if x+1 < N and y+1 < N and house[x+1][y+1] == 0 and house[x][y+1] == 0 and house[x+1][y] == 0:
            dfs((x+1, y+1, 2))

# DFS 함수 실행
# 파이프는 항상 (1, 1), (1, 2)에 놓여있다. 즉, 0, 1부터 파이프를 움직이면 된다.
# X, Y, direction(Z)
dfs((0, 1, 0))

# 결과출력
print(count)