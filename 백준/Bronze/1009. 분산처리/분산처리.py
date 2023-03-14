import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = map(int, input().split())
    if b < 4:
        if str(a**b)[-1] == '0':
            print(10)
        else:
            print(str(a**b)[-1])
    else:
        c = b % 4
        if c == 0:
            c = 4
        if str(a**c)[-1] == '0':
            print(10)
        else:
            print(str(a**c)[-1])