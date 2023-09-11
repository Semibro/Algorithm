A = int(input())
B = int(input())
answer = 0

if A >= 20:
    answer += 24-A
    answer += B
if A <= 3:
    answer += B -A

print(answer)