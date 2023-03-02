K, N = map(int, input().split())
lst = []
for _ in range(K):
    lst.append(int(input()))

max_v = max(lst)
min_v = 1
result = []
while min_v <= max_v:
    middle = (max_v + min_v) // 2
    cnt = 0
    for i in lst:
        cnt += i // middle
    if cnt >= N:
        result.append(middle)
        min_v = middle + 1
    else:
        max_v = middle - 1

print(max(result))