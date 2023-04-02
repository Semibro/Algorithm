N = int(input())
lst = list(map(int, input().split()))
result = 0
for i in lst:
    if i == N:
        result += 1
print(result)