N = int(input())
A = list(map(int, input().split()))

visited = [False] * (N + 1)
answer, start = 0, 0

for end in range(N):
    while visited[A[end]]:
        visited[A[start]] = False
        start += 1

    visited[A[end]] = True
    answer += (end - start + 1)

print(answer)