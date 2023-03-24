import sys

n = int(sys.stdin.readline())
color = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

zero_count = 0
one_count = 0
minus_count = 0


def divideandconquer(x, y, n):
    global zero_count, one_count, minus_count
    samecolor = color[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if samecolor != color[i][j]:
                divideandconquer(x, y, n // 3)
                divideandconquer(x, y + n // 3, n // 3)
                divideandconquer(x + n // 3, y, n // 3)
                divideandconquer(x + n // 3, y + n // 3, n // 3)
                divideandconquer(x, y + n // 3 + n // 3, n // 3)
                divideandconquer(x + n // 3 + n // 3, y, n // 3)
                divideandconquer(x + n // 3 + n // 3, y + n // 3, n // 3)
                divideandconquer(x + n // 3, y + n // 3 + n // 3, n // 3)
                divideandconquer(x + n // 3 + n // 3, y + n // 3 + n // 3, n // 3)
                return

    if samecolor == 0:
        zero_count += 1
    elif samecolor == 1:
        one_count += 1
    else:
        minus_count += 1


divideandconquer(0, 0, n)
print(minus_count)
print(zero_count)
print(one_count)