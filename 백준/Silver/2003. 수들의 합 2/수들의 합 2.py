N, M = map(int, input().split())
A = list(map(int, input().split()))

total, end, answer = A[0], 0, 0
for start in range(N):
    while end < N - 1 and total < M:
        end += 1
        total += A[end]

    if end == N:
        break

    if total == M:
        answer += 1

    total -= A[start]

print(answer)