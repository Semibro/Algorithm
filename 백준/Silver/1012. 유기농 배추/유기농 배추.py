t = int(input())
for _ in range(t):
    M, N, K = map(int, input().split())
    ground = [[0] * (M+2) for _ in range(N+2)]
    visited = [[False] * (M+2) for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y+1][X+1] = 1

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    stack = []
    cnt = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            if ground[i][j] == 1 and not visited[i][j]:
                while True:
                    visited[i][j] = True
                    for k in delta:
                        if ground[i + k[0]][j + k[1]] == 1:
                            if not visited[i + k[0]][j + k[1]]:
                                stack.append([i, j])
                                i = i + k[0]
                                j = j + k[1]
                                break

                    else:
                        if stack:
                            v = stack.pop()
                            i, j = v[0], v[1]
                        else:
                            cnt += 1
                            break

    print(cnt)