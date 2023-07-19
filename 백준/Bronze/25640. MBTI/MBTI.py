x = input()
n = int(input())
answer = 0
for _ in range(n):
    y = input()
    if x == y:
        answer += 1
        
print(answer)