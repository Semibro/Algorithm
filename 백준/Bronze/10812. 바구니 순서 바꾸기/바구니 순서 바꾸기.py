N, M = map(int, input().split())
arr = []
for i in range(N+1):
    arr.append(i)
for _ in range(M):
    a, b, c = map(int, input().split())
    tmp1 = arr[c:b+1]
    tmp2 = arr[a:c]
    arr[a:b+1] = tmp1+tmp2
print(*arr[1:])