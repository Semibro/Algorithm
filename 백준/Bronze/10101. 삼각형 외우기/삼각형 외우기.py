x = []
for _ in range(3):
    x.append(int(input()))

if x.count(60) == 3:
    print('Equilateral')
else:
    if sum(x) == 180:
        if x[0] != x[1] and x[1] != x[2] and x[0] != x[2]:
            print('Scalene')
        else:
            print('Isosceles')
    else:
        print('Error')