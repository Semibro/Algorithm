C, R = map(int, input().split())
K = int(input())

seat = [[0]*(R+2) for _ in range(C+2)]
for i in range(0, C+2):
    if i == 0 or i == (C+1):
        arr = [1] * (R+2)
        seat[i] = arr
    else:
       seat[i][0], seat[i][-1] = 1, 1

Idx = 0
delta = [(0, 1), (-1, 0), (0, -1), (1, 0)]
sx, sy, var = 1, 0, 0
if C*R < K:
    print(0)
else:
    while True:
        if K == Idx:
            break
        else:
            for i in range(0, C*R):
                if seat[sx+delta[var][0]][sy+delta[var][1]] != 0:
                    for d in range(4):
                        if seat[sx+delta[d][0]][sy+delta[d][1]] == 0:
                            var = d
                else:
                    seat[sx+delta[var][0]][sy+delta[var][1]] = seat[sx][sy] + 1
                    sx += delta[var][0]
                    sy += delta[var][1]
                    Idx += 1
                    if Idx == K:
                        break
    print(sx, sy)