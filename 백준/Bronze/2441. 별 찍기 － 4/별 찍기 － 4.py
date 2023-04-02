N = int(input())
idx = 0
for i in range(N, 0, -1):
    print(f'{" "*idx+"*"*i}')
    idx += 1