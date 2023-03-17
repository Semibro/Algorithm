import sys
n = int(sys.stdin.readline())
color = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

white_count = 0
blue_count = 0

def divideandconquer(x, y, n):
    global white_count, blue_count
    samecolor = color[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if samecolor != color[i][j]:
                divideandconquer(x, y, n//2)
                divideandconquer(x, y+n//2, n//2)
                divideandconquer(x+n//2, y, n//2)
                divideandconquer(x+n//2, y+n//2, n//2)
                return
                
    if samecolor == 0:
        white_count += 1
    else:
        blue_count += 1

divideandconquer(0, 0, n)
print(white_count)
print(blue_count)