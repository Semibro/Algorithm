N = int(input())
lst = list(map(int, input().split()))
result = []
up = down = 1
if len(lst) > 1:
    for i in range(N-1):
        if lst[i] < lst[i+1]:
            result.append(down)
            down = 1
            up += 1
            result.append(up)
        elif lst[i] == lst[i+1]:
            down += 1
            up += 1
            result.append(up)
            result.append(down)
        else:
            result.append(up)
            up = 1
            down += 1
            result.append(down)
else:
    result.append(1)
print(max(result))