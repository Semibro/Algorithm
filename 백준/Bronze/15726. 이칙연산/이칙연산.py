A, B, C = map(int, input().split())
X = A * B / C
Y = A / B * C
if X > Y:
    print(int(X))
else:
    print(int(Y))