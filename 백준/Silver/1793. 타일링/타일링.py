def rectangle(n):
    f = [0] * (251)
    f[0] = 1
    f[1] = 1
    f[2] = 3
    for i in range(3, n+1):
        f[i] = f[i-1] + (2*f[i-2])
    return f[n]

while True:
    try:
        tc = int(input())
        print(rectangle(tc))
    except:
        break