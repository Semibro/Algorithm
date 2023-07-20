A, B, C = map(int, input().split())
D, E, F = map(int, input().split())

answer = 0
if A < D:
    answer += D-A
if B < E:
    answer += E-B
if C < F:
    answer += F-C
print(answer)