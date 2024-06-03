N, K = map(int, input().split())
lst = list(map(int, input().split()))

check = dict()
start, end, max_length = 0, 0, 0

while end < N:
    if lst[end] not in check:
        check[lst[end]] = 0

    if check[lst[end]] == K:
        check[lst[start]] -= 1
        start += 1
    else:
        check[lst[end]] += 1
        end += 1

    max_length = max(max_length, end-start)

print(max_length)