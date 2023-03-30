N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [0] * (N+1)
result = []

def backtracking(cnt):
    if cnt == M:
        res = []
        for i in range(len(lst)):
            if visited[i] == 1:
                res.append(lst[i])
        result.append(tuple(res))
        return
    else:
        for i in range(len(lst)):
            if not visited[i]:
                visited[i] = 1
                backtracking(cnt+1)
                visited[i] = 0

backtracking(0)
for i in list(set(result)):
    print(*i)