import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = []
MIN = float("inf")

for _ in range(N):
    A.append(int(input()))

A.sort()
end = 0

for start in range(N):
    while end < N and A[end] - A[start] < M:
        end += 1

    if end == N:
        break

    MIN = min(MIN, A[end] - A[start])

print(MIN)