T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    while x <= M*N:
        if (x-y) % N == 0:
            print(x)
            break
        x += M
    else:
        print(-1)