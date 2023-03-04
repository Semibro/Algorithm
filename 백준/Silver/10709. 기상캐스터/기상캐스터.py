H, W = map(int, input().split())
sky = [input() for _ in range(H)]
result = [[-1] * W for _ in range(H)]
for i in range(H):
    for j in range(W-1, -1, -1):
        if sky[i][j] == 'c':
            result[i][j] = 0
        else:
            cnt = 0
            for k in range(j-1, -1, -1):
                if sky[i][k] == 'c':
                    cnt += j-k
                    break
            if cnt == 0:
                pass
            else:
                result[i][j] = cnt
for i in result:
    print(*i)