n = int(input())
answer = {}

for _ in range(n):
    people, log = input().split()

    answer[people] = log
    if log == 'leave':
        del answer[people]
    
temp = sorted(answer.keys(), reverse=True)


for item in temp:
    print(item)