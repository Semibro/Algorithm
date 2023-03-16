M = int(input())
N = int(input())
result = []
for i in range(M, N+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        if i == 1:
            pass
        else:
            result.append(i)
if len(result) > 0:
    print(sum(result))
    print(result[0])
else:
    print(-1)