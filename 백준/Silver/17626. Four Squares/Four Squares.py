arr = [0, 1, 2, 3]
for i in range(4, 50001):
    if i**0.5 == int(i**0.5):
        arr.append(1)
    else:
        lst = []
        res = 5
        for j in range(1, int(i**0.5)+1):
            lst.append(j)
        for k in lst:
            if res > 1+arr[i-k**2]:
                res = 1+arr[i-k**2]
        arr.append(res)
print(arr[int(input())])