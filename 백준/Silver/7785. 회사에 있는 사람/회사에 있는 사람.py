n = int(input())
answer = {}

for _ in range(n):
    people, log = input().split()

    answer[people] = log
    if log == 'leave':
        del answer[people]
    
temp = sorted(answer.items(), reverse=True)
ans = dict(temp)


for item in ans.keys():
    print(item)