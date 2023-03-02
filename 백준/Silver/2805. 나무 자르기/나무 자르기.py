N, M = map(int, input().split())
tree = list(map(int, input().split()))

max_v = max(tree)
min_v = 1
result = [0]

while min_v <= max_v:
    middle = (max_v + min_v) // 2
    cnt = 0
    for i in tree:
        if i - middle >= 0:
            cnt += i - middle
    if cnt >= M:
        result.append(middle)
        min_v = middle + 1
    else:
        max_v = middle - 1

print(max(result))