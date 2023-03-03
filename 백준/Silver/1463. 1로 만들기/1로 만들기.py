recur = [0, 0, 1, 1]
N = int(input())
for i in range(4, N+1):
    if i % 6 == 0:
        if recur[i//3] < recur[i//2]:
            if recur[i-1] < recur[i//3]:
                recur.append(recur[i-1]+1)
            else:
                recur.append(recur[i//3]+1)
        else:
            if recur[i-1] < recur[i//2]:
                recur.append(recur[i-1] + 1)
            else:
                recur.append(recur[i//2] + 1)
    else:  # 안나눠짐
        if i % 3 == 0:
            if recur[i - 1] < recur[i//3]:
                recur.append(recur[i-1] + 1)
            else:
                recur.append(recur[i//3] + 1)
        elif i % 2 == 0:
            if recur[i - 1] < recur[i//2]:
                recur.append(recur[i-1] + 1)
            else:
                recur.append(recur[i//2] + 1)
        else:
            recur.append(recur[i-1] + 1)
print(recur[N])