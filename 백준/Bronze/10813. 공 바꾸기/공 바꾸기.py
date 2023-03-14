N, M = map(int, input().split())
lst = []
for i in range(N+1):
    lst.append(i)
for i in range(M):
    a, b = map(int, input().split())
    tmp = lst[a]
    tmp2 = lst[b]
    lst[a] = tmp2
    lst[b] = tmp
print(*lst[1:])