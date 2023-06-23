N, W, H, L = map(int, input().split())
answer = (W//L) * (H//L)
if answer >= N:
    print(N)
else:
    print(answer)