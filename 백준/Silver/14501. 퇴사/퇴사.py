N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int, input().split())

answer = 0

def dfs(n, sm):
    global answer
    # 종료조건
    if n >= N:
        answer = max(answer, sm)
        return
    # 백트래킹
    else:
        # 상담하는 경우
        if n + T[n] <= N:
            dfs(n+T[n], sm+P[n])
        # 상담하지 않는 경우
        dfs(n+1, sm)

dfs(0, 0)
print(answer)