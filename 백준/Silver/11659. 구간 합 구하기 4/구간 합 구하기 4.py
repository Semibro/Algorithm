import sys
imput = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
arr = [lst[0]]
for i in range(1, N):
    arr.append(lst[i] + arr[i-1])
for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    if x-1 < 0:
        print(arr[y])
    else:
        print(arr[y] - arr[x-1])