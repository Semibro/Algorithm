J, R = map(int, input().split())
point = list(map(int, input().split()))
result = [0] * J

for i in range(J):
    for j in range(R):
        result[i] += point[i+j*J]

count = 0
for i in range(J-1, -1, -1):
    if max(result) == result[i]:
        print(J-count)
        break
    else:
        count += 1