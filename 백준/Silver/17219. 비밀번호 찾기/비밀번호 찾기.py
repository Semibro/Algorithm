import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = {}
for _ in range(N):
    link, pw = input().split()
    arr[link] = pw
for _ in range(M):
    x = str(input().rstrip())
    print(arr[x])