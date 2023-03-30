N, M = map(int, input().split())
visited = [0] * (N+1)
result = []

def backtracking(cnt):
    if cnt == M:
        res = []
        for i in range(1, N+1):
            if visited[i] == 1:
                res.append(i)
        result.append(tuple(res))
        return
    else:
        for i in range(1, N+1):
            if not visited[i]:
                visited[i] = 1
                backtracking(cnt+1)
                visited[i] = 0

backtracking(0)
for i in list(set(result)):
    print(*i)