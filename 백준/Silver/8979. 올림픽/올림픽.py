# N: 국가의 수  / K: 등수를 알고 싶은 국가
N, K = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x: x[1:], reverse=True)
# [[1, 1, 2, 0], [2, 0, 1, 0], [3, 0, 1, 0], [4, 0, 0, 1]]
for i in range(N):
    if lst[i][0] == K:
        idx = i

for i in range(N):
    if lst[i][1:] == lst[idx][1:]:
        print(i+1)
        break