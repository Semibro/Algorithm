D, K = map(int, input().split())
s = 0
for A in range(1, 100000):
    arr = [0] * 100001
    if s == 1:
        break
    else:
        for B in range(A, 100001):
            arr[0] = A
            arr[1] = B
            for i in range(2, D):
                arr[i] = arr[i-1] + arr[i-2]
            if arr[D-1] == K:
                print(arr[0])
                print(arr[1])
                s = 1
                break