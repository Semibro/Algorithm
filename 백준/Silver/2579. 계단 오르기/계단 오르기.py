x = int(input())
stairs = []
dp = [0] * 301
for _ in range(x):
    stairs.append(int(input()))
if x == 1:
    print(stairs[0])
elif x == 2:
    print(stairs[0]+stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3, x):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[x-1])