H, W, X, Y = map(int, input().split())
B_lst = []
for i in range(H+X):
    B_lst.append(list(map(int, input().split())))
# lst :  [[1, 2, 3, 4, 0], [5, 7, 9, 11, 4], [0, 5, 6, 7, 8]]

A_lst = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        A_lst[i][j] = B_lst[i][j]

for i in range(X, H):
    for j in range(Y, W):
        A_lst[i][j] = B_lst[i][j] - A_lst[i-X][j-Y]

for i in range(H):
    for j in range(W):
        print(A_lst[i][j], end=" ")
    print("")