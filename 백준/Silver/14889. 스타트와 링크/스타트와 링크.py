def check(lst, lst2):
    global res
    min_1, min_2 = 0, 0
    for i in range(N//2-1):
        for j in range(i+1, N//2):
            min_1 += arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]]
            min_2 += arr[lst2[i]][lst2[j]] + arr[lst2[j]][lst2[i]]
    res = min(res, abs(min_1-min_2))
    return



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
result = []


def bt(cnt, res, idx):
    if cnt == N//2:
        result.append(res[:])
        return
    else:
        for j in range(idx, N):
            if not visited[j]:
                visited[j] = 1
                res.append(j)
                bt(cnt+1, res, j)
                res.pop()
                visited[j] = 0

bt(0, [], 0)
res = 9876543210
for i in range(len(result)//2):
    check(result[i], result[-i-1])
print(res)
