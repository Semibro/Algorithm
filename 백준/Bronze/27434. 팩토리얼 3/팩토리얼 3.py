import sys
n = int(sys.stdin.readline())
result = 1
for i in range(n, 0, -1):
    result *= i
print(result)