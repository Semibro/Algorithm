import sys
input = sys.stdin.readline
n, m = map(int, input().split())
money = list(map(int, input().split()))
result = [0] * (n-m+1)
result[0] = sum(money[0:m])
for i in range(1, n-m+1):
    result[i] = result[i-1]-money[i-1]+money[i+m-1]
print(max(result))