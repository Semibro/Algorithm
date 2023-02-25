def change(num):
    if switch[num] == 1:
        switch[num] = 0
    else:
        switch[num] = 1

N = int(input())  # 스위치 개수
switch = [0] + list(map(int, input().split()))
M = int(input())  # 학생수
for _ in range(M):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1: 
                break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

for i in range(1, N+1):
    print(switch[i], end = ' ')
    if i % 20 == 0:
        print()