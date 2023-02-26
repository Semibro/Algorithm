import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
result = []
bin_lst = lst[0:K]
result.append(sum(bin_lst))
for i in range(K, N):
    bin_lst.pop(0)
    bin_lst.append(lst[i])
    result.append(sum(bin_lst))

print(max(result))