import math
N = input()
cnt = 0
tmp = 0
lst = [0] * 10
for i in range(10):
    if i == 6:
        tmp += N.count(str(i))
    elif i == 9:
        tmp += N.count(str(i))
        lst[i] = math.ceil(tmp/2)
    else:
        lst[i] = N.count(str(i))
print(max(lst))