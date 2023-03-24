import sys

n = int(input())
color = [input() for _ in range(n)]

result = ''


def divideandconquer(x, y, n):
    global result
    samecolor = color[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if samecolor != color[i][j]:
                result += '('
                divideandconquer(x, y, n//2)
                divideandconquer(x, y + n//2, n//2)
                divideandconquer(x + n//2, y, n//2)
                divideandconquer(x + n//2, y + n//2, n//2)
                result += ')'
                return
    if samecolor == '0':
        result += '0'
    else:
        result += '1'


divideandconquer(0, 0, n)
print(result)