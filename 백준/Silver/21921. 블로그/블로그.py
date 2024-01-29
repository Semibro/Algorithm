N, X = map(int, input().split())
day = list(map(int, input().split()))

for i in range(1, N):
    day[i] += day[i-1]

max_value, count = day[X-1], 1
for i in range(X, N):
    if max_value < day[i] - day[i-X]:
        max_value = day[i] - day[i-X]
        count = 1
    elif max_value == day[i] - day[i-X]:
        count += 1

if max_value == 0:
    print('SAD')
else:
    print(max_value)
    print(count)