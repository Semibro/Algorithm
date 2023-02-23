N, M = map(int, input().split())
result = [0] * (N+1)
for _ in range(M):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        result[l] = k

print(*result[1:])