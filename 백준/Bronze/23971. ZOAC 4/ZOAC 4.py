H, W, N, M = map(int, input().split())
answer = 1

if H % (N+1) > 0:
    answer = answer * (H//(N+1) + 1)
else:
    answer = answer * H//(N+1)
if W % (M+1) > 0:
    answer = answer * (W//(M+1) + 1)
else:
    answer = answer * W//(M+1)

print(answer)