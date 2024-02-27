N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
min_space = [[[9876543210] * 3 for _ in range(M)] for _ in range(N)]

# 처음 시작값 설정
for i in range(M):
    min_space[0][i] = [space[0][i], space[0][i], space[0][i]]

# DP
for i in range(1, N):
    for j in range(M):
        for k in range(3):
            # 예외처리
            if (j==0 and k==2) or (j==M-1 and k==0):
                continue
            for l in range(3):
                if k!=l:
                    min_space[i][j][k] = min(min_space[i][j][k], min_space[i-1][j-k+1][l] + space[i][j])

answer = 9876543210
for i in range(M):
    answer = min(min(min_space[N-1][i]), answer)

print(answer)