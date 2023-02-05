t, s = map(int, input().split())

if s == 1:
    print(280)
else:
    if t >= 12 and t <= 16:
        print(320)
    else:
        print(280)