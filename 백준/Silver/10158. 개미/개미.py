import sys
input = sys.stdin.readline

garo, sero = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

x = x + t
y = y + t

if (x//garo) % 2 == 0:
    x = x % garo
else :
    x = garo - (x%garo)

if (y//sero) % 2 == 0:
    y = y % sero
else :
    y = sero - (y % sero)

print(x, y)