def binary(n):
    x = format(n, 'b')
    result = 0
    l = len(x)
    for i in range(l-1, -1, -1):
        if x[i] == '1':
            result += 4**(l-i-1)
    return result

N, r, c = map(int, input().split())
print(binary(r)*2 + (binary(c)))