arr = [1, 1, 1]
for i in range(3, 101):
    arr.append(arr[i-2] + arr[i-3])
for _ in range(int(input())):
    print(arr[int(input())-1])