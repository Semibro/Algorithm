N, M = map(int, input().split())
bung = [input() for _ in range(N)]
for idx in range(N):
    print(bung[idx][::-1])