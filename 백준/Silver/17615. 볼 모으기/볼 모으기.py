N = int(input())
balls = input()
RedBall, BlueBall, answer = balls.count('R'), balls.count('B'), 9876543210

# CASE 1
cnt = 0
flag = True  # 빨간공 True, 파란공 False

for i in range(N):
    if i == 0:
        if balls[i] == 'B':
            flag = False
        cnt += 1
    else:
        if balls[i] == 'R':
            if flag == True:
                cnt += 1
            else:
                break
        else:
            if flag == False:
                cnt += 1
            else:
                break

if flag == True:
    answer = min(answer, RedBall-cnt)
else:
    answer = min(answer, BlueBall-cnt)

# CASE 2
cnt = 0
flag = True

for i in range(N-1, -1, -1):
    if i == N-1:
        if balls[i] == 'B':
            flag = False
        cnt += 1
    else:
        if balls[i] == 'R':
            if flag == True:
                cnt += 1
            else:
                break
        else:
            if flag == False:
                cnt += 1
            else:
                break

if flag == True:
    answer = min(answer, RedBall-cnt)
else:
    answer = min(answer, BlueBall-cnt)

print(min(answer, RedBall, BlueBall))