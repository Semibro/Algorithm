while True:
    one, two, three = map(int, input().split())
    if one == 0 and two == 0 and three == 0:
        break
    else:
        if one == two and two == three:
            print('Equilateral')
        else:
            if one == max(one, two, three):
                if one >= two + three:
                    print('Invalid')
                else:
                    if one == two or two == three or three == one:
                        print('Isosceles')
                    else:
                        print('Scalene')
            elif two == max(one, two, three):
                if two >= one + three:
                    print('Invalid')
                else:
                    if one == two or two == three or three == one:
                        print('Isosceles')
                    else:
                        print('Scalene')
            else:
                if three >= one + two:
                    print('Invalid')
                else:
                    if one == two or two == three or three == one:
                        print('Isosceles')
                    else:
                        print('Scalene')