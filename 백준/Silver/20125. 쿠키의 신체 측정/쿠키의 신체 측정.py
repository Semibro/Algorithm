N = int(input())
x, y, Larm, Rarm, core, Lleg, Rleg = 0, 0, 0, 0, 0, 0, 0

for i in range(N):
    for j, cookie in enumerate(list(input())):
        if x == 0 and y == 0 and cookie == '*':
            x, y = i+1, j
        elif i == x and j < y and cookie == '*':
            Larm += 1
        elif i == x and j > y and cookie == '*':
            Rarm += 1
        elif i > x and j == y and cookie == '*':
            core += 1
        elif i > x+core and j < y and cookie == '*':
            Lleg += 1
        elif i > x+core and j > y and cookie == '*':
            Rleg += 1

print(x+1, y+1)
print(Larm, Rarm, core, Lleg, Rleg)