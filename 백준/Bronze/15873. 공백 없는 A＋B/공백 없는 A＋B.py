na = input()
if '0' in na:
    if na.count('0') == 1:
        if na.index('0') == 1:
            print(int(na[:2]) + int(na[2]))
        else:
            print(int(na[0]) + int(na[1:]))
    else:
        print(20)
else:
    print(int(na[0]) + int(na[1]))