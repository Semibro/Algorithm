n = int(input())
if n == 4:
    print('long int')
else:
    a = n // 4
    print('long ' * (a-1), end = '')
    print('long int')