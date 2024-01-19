dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]
for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(int(input())):
    n = int(input())
    '''
    1 -> 1
    2 -> 2
    3 -> 3
    4 -> 4
    5 -> 5
    6 -> 7 (111111, 21111, 2211, 222, 3111, 321, 33)
    '''
    print(dp[n])