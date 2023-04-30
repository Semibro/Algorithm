n = int(input())
result = n % 8
if result == 1:
    print(1)
elif result == 2 or result == 0:
    print(2)
elif result == 3 or result == 7:
    print(3)
elif result == 4 or result == 6:
    print(4)
else:
    print(5)