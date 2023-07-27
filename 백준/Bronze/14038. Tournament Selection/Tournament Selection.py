win = 0
for _ in range(6):
    if input() == 'W':
        win += 1
if win == 0:
    print(-1)
else:
    if win >= 5:
        print(1)
    elif win >= 3:
        print(2)
    else:
        print(3)