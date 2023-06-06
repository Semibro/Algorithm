N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0

flag1 = 1

while flag1 == 1:
    # 현재 위치 청소
    room[r][c] = 2
    answer += 1

    # 왼쪽방향으로 순서대로 탐색 후 청소시작
    flag2 = 1
    while flag2 == 1:
        for id in ((d+3)%4, (d+2)%4, (d+1)%4, d):
            ir, ic = r+delta[id][0], c+delta[id][1]
            if room[ir][ic] == 0:  # 미청소
                r, c, d = ir, ic, id
                flag2 = 0
                break
        else:  # 4방향 모두 미청소 영역이 아닐 경우
            # 후진
            br, bc = r-delta[d][0], c-delta[d][1]
            if room[br][bc] == 1:
                flag1 = 0
                break
            else:
                r, c = br, bc


print(answer)