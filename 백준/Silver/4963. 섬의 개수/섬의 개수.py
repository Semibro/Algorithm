while True:
    W, H = map(int, input().split())
    if W + H == 0:
        break
    else:
        # input
        board = [[0] + list(map(int, input().split())) + [0]for _ in range(H)]
        island = [[0] * (W+2)] + board + [[0] * (W+2)]

        # setting
        delta = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        visited = [[False] * (W+2) for _ in range(H+2)]
        stack = []
        cnt = 0

        # dfs
        for i in range(1, H+1):
            for j in range(1, W+1):
                if island[i][j] == 1 and not visited[i][j]:
                    while True:
                        visited[i][j] = True
                        for k in delta:
                            if island[i+k[0]][j+k[1]] == 1:
                                if not visited[i+k[0]][j+k[1]]:
                                    stack.append([i, j])
                                    i = i+k[0]
                                    j = j+k[1]
                                    break
                        else:
                            if stack:
                                v = stack.pop()
                                i, j = v[0], v[1]
                            else:
                                cnt += 1
                                break

        print(cnt)