x = list(map(int, input().split()))
one, two = x.count(1), x.count(2)
if one > two:
    print(1)
else:
    print(2)