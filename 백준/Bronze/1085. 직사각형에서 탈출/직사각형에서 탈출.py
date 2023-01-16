X, Y, W, H = map(int, input().split())

print(min(X, Y, W-X, H-Y))