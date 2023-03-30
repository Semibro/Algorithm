N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = []
visited = [0] * (N+1)

def backtracking(cnt, res):
    if cnt == M:
        result.append(tuple(res[:]))
        return
    else:
        for i in range(len(lst)):
            if not visited[i]:
                visited[i] = 1
                res.append(lst[i])
                backtracking(cnt + 1, res)
                res.pop()
                visited[i] = 0
backtracking(0, [])
for i in list(set(result)):
    print(*i)