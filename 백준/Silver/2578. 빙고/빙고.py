def check():
    # 대각선 and 가로
    b = 0
    if bingo[0][0] + bingo[1][1] + bingo[2][2] + bingo[3][3] + bingo[4][4] == 0:
        b += 1
    if bingo[4][0] + bingo[3][1] + bingo[2][2] + bingo[1][3] + bingo[0][4] == 0:
        b += 1
    for i in bingo:
        if sum(i) == 0:
            b += 1
            if b == 3:
                return True
    # 세로
    for i in range(5):
        res = -1
        for j in range(5):
            res += bingo[j][i]
        if res < 0:
            b += 1
            if b == 3:
                return True
    return False

bingo = [list(map(int, input().split())) for _ in range(5)]
social = list(map(int, input().split()))
for _ in range(4):
    social += list(map(int, input().split()))
ans = 0

for k in range(25):
    if ans > 0:
        break
    for i in range(5):
        if ans > 0:
            break
        for j in range(5):
            if bingo[i][j] == social[k]:
                bingo[i][j] = 0
                if check():
                    ans += k
                    break

print(ans+1)