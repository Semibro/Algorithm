def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        s = 0
        for j in range(i):
            s += dp[j] * dp[i - 1 -j]
        dp[i] = s
    return dp[n]