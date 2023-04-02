N = int(input())
idx = N-1
for i in range(1, 2*N):
    if i <= N:
        res = ('*'*i) + (' '*abs(N-i))
        print(res+res[::-1])
    else:
        res = ('*'*idx) + (' '*abs(N-i))
        print(res+res[::-1])
        idx -= 1