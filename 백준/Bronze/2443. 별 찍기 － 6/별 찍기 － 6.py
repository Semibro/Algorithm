N = int(input())
idx = 1
for i in range(N, 0, -1):
    print(f'{" "*(N-i)+"*"*(2*N-idx)}')
    idx += 2