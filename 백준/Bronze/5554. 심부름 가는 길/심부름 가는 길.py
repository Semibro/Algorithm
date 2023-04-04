move = 0
for _ in range(4):
    sec = int(input())
    move += sec
print(move//60)
print(move%60)