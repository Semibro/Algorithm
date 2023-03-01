N, K = map(int, input().split())
lst = [0] * 12  # [여1, 여2, 여3, 여4, 여5, 여6, 남1, 남2, 남3, 남4, 남5, 남6]
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        if Y == 1:
            lst[0] += 1
        elif Y == 2:
            lst[1] += 1
        elif Y == 3:
            lst[2] += 1
        elif Y == 4:
            lst[3] += 1
        elif Y == 5:
            lst[4] += 1
        else:
            lst[5] += 1
    else:
        if Y == 1:
            lst[6] += 1
        elif Y == 2:
            lst[7] += 1
        elif Y == 3:
            lst[8] += 1
        elif Y == 4:
            lst[9] += 1
        elif Y == 5:
            lst[10] += 1
        else:
            lst[11] += 1

cnt = 0
for i in lst:
    if 0 < i <= K:
        cnt += 1
    elif i > K:
        cnt += (i//K + i%K)

print(cnt)