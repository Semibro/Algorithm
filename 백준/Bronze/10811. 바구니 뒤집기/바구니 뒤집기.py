N, M = map(int, input().split())
lst = []
for i in range(N+1):
    lst.append(i)
for i in range(M):
    a, b = map(int, input().split())
    tmp = lst[a:b+1]
    lst[a:b+1] = tmp[::-1]
print(*lst[1:])