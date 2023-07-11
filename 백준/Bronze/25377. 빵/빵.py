N = int(input())
result = 9876543210
for _ in range(N):
    s, e = map(int, input().split())
    if s <= e:
        result = min(result, e)
if result == 9876543210:
    print(-1)
else:
    print(result)