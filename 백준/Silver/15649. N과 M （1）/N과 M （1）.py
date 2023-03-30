N, M = map(int, input().split())
visited = [0] * (N+1)
result = []

def backtracking(cnt, res):
    if cnt == M:
        result.append(res[:])
        return
    else:
        for i in range(1, N+1):
            if not visited[i]:
                visited[i] = 1
                res.append(i)
                backtracking(cnt+1, res)
                res.pop()
                visited[i] = 0

backtracking(0, [])
for i in result:
    print(*i)