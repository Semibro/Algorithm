lst = list(map(int, input().split()))
x, y, r = map(int, input().split())

if x in lst:
    print(lst.index(x) + 1)
else:
    print(0)