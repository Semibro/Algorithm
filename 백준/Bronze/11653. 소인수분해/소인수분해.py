N = int(input())
if N == 1:
    print()
else:
    x = N
    for i in range(2, N+1):
        if x % i == 0:
            while True:
                if x % i != 0:
                    break
                else:
                    print(i)
                    x = x//i