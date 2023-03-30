N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = []

def backtracking(cnt, res):
    if cnt == M:
        result.append(res[:])
        return
    else:
        for i in range(len(lst)):
            if len(res) == 0:
                res.append(lst[i])
                backtracking(cnt + 1, res)
                res.pop()
            else:
                if lst[i] >= res[-1]:
                    res.append(lst[i])
                    backtracking(cnt+1, res)
                    res.pop()
backtracking(0, [])
for i in result:
    print(*i)