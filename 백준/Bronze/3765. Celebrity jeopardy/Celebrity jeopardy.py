result = []
while True:
    try:
        a = input()
        result.append(a)
    except EOFError:
        break
for i in result:
    print(i)