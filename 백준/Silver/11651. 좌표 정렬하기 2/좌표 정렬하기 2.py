n = int(input())
result_lst = []
for i in range(n):
    x, y = map(int, input().split())
    result_lst.append((x, y))

sorted_lst = sorted(result_lst, key = lambda x: (x[1], x[0]))
for j in range(len(sorted_lst)):
    print(*sorted_lst[j])