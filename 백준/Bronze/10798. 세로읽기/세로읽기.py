lst = []
for _ in range(5):
    x = list(input())
    lst.append(x)
max_l = 0
ans = ''
for i in lst:
    if max_l < len(i):
        max_l = len(i)
for i in range(max_l):
    for j in range(5):
        try:
            ans += lst[j][i]
        except:
            pass
print(ans)