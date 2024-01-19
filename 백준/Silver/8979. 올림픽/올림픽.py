# N: 국가의 수  / K: 등수를 알고 싶은 국가
N, K = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))
temp_lst = lst[K-1]
lst.sort(reverse=True)
print(lst.index(temp_lst)+1)