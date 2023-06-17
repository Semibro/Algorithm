A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
answer = 0

if A < 0:
    answer += C * abs(A)
    answer += D
    answer += E * B
else:
    answer += (B-A) * E
print(answer)