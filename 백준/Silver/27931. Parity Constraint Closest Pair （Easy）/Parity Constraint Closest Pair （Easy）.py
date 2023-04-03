N = int(input())
lst = list(map(int, input().split()))
lst.sort()
min_jj, min_h = 9876543210, 9876543210
for i in range(N-1):
    for j in range(i+1, N):
        if (lst[j]-lst[i]) % 2 == 0:
            min_jj = min(min_jj, lst[j]-lst[i])
        else:
            min_h = min(min_h, lst[j]-lst[i])
if min_h == 9876543210:
    min_h = -1
if min_jj == 9876543210:
    min_jj = -1
print(min_jj, min_h)