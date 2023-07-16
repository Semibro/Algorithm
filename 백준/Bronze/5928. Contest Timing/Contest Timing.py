D, H, M = map(int, input().split())

time_1 = D*24*60 + H*60 + M
time_2 = 11*24*60 + 11*60 + 11

time = time_1 - time_2
if time < 0:
    print(-1)
else:
    print(time)