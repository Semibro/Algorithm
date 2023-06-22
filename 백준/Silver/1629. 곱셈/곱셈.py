import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

def divideandconquer(x, y, z):
    if y == 1:
        return x%z
    else:
        t = divideandconquer(x, y//2, z)
        if y % 2 == 0:
            return (t * t) % z
        else:
            return (t * t * x) % z

print(divideandconquer(A, B, C))