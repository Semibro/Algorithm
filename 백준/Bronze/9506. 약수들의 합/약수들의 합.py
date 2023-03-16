while True:
    n = int(input())
    if n == -1:
        break
    else:
        result = []
        for i in range(1, n):
            if n % i == 0:
                result.append(i)
        if sum(result) != n:
            print(f'{n} is NOT perfect.')
        else:
            res = ''
            for i in result:
                res += f'{i} + '
            print(f'{n} = {res[:-3]}')