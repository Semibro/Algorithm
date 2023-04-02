N = int(input())
idx = 1
idx2 = N-1
for i in range(2*N-1):
    if i < N-1:
        print(f'{" "*i + "*"*(2*N-idx)}')
        idx += 2
    else:
        print(f'{" "*idx2 + "*"*(2*N-idx)}')
        idx -= 2
        idx2 -= 1