N = int(input())
A, B, C = map(int, input().split())

answer = 0
if A <= N:
    answer += A
else:
    answer += N
if B <= N:
    answer += B
else:
    answer += N
if C <= N:
    answer += C
else:
    answer += N
    
print(answer)