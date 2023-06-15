import sys
input = sys.stdin.readline

N = int(input())
S = int(input())
M = input()

check = 'IOI' + 'OI'*(N-1)
answer = 0

for i in range(0, S-(2*N)):
    if M[i:i+3+(2*(N-1))] == check:
        answer += 1

print(answer)