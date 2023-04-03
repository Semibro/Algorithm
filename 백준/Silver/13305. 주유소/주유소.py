N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
result = 0
min_V = oil[0]
for i in range(N-1):
    if min_V > oil[i]:
        min_V = oil[i]
    result += min_V * road[i]
print(result)