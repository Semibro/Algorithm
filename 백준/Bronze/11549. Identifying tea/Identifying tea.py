T = int(input())
lst = list(map(int, input().split()))
answer = 0
for i in lst:
    if i == T:
        answer += 1
        
print(answer)