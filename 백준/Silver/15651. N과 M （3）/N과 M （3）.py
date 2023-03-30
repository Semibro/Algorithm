N, M = map(int, input().split())
result = []

def backtracking(cnt, res):
    if cnt == M:
        result.append(res[:])
        return
    else:
        for i in range(1, N+1):
            res.append(i)
            backtracking(cnt+1, res)
            res.pop()

backtracking(0, [])
for i in result:
    print(*i)