N = int(input())
if N == 0:
    print(0)
else:
    fact = 1
    for i in range(1, N+1):
        fact *= i
        count = 0
    f = str(fact)
    for i in range(len(f)-1, -1, -1):
        if f[i] == '0':
            count += 1
        else:
            print(count)
            break