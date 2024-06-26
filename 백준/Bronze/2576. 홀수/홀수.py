min_value, sum_value = 9876543210, 0

for _ in range(7):
    nn = int(input())
    if nn % 2 != 0:
        min_value = min(min_value, nn)
        sum_value += nn

if sum_value == 0:
    print(-1)
else:
    print(sum_value)
    print(min_value)