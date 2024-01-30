number = input()
N = 0

while True:
    N += 1
    num = str(N)

    while len(number) > 0 and len(num) > 0:
        if num[0] == number[0]:
            number = number[1:]
        num = num[1:]

    if number == "":
        print(N)
        break