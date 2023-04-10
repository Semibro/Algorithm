while True:
    x = list(map(int, input().split()))
    if sum(x) == 0:
        break
    else:
        print(sum(x))