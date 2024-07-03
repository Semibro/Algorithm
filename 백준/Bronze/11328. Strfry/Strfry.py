N = int(input())

for _ in range(N):
    ipt = list(input().split())
    a, b = list(ipt[0]), list(ipt[1])
    a.sort()
    b.sort()

    if a == b:
        print('Possible')
    else:
        print('Impossible')