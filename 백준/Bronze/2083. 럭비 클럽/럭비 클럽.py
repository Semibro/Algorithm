while True:
    name, age, weight = input().split()
    if name == '#':
        break
    else:
        a = int(age)
        w = int(weight)
        if a > 17 or w >= 80:
            print(f'{name} Senior')
        else:
            print(f'{name} Junior')