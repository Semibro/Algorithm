N = int(input())
x = 2*N-1
idx = 1
for i in range(1, 2*N):
    print(' ' * abs(N-i) + '*'*idx)
    if i < N:
        idx += 2
    elif i >= N:
        idx -= 2