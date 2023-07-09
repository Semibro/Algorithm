Apple, Banana = 0, 0

Apple += int(input()) * 3
Apple += int(input()) * 2
Apple += int(input())

Banana += int(input()) * 3
Banana += int(input()) * 2
Banana += int(input())

if Apple > Banana:
    print('A')
elif Banana > Apple:
    print('B')
else:
    print('T')