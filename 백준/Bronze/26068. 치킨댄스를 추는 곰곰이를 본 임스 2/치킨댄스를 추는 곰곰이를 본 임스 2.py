t = int(input())
answer = 0

for _ in range(t):
    x = input()
    if int(x[2:]) <= 90:
        answer += 1
        
print(answer)