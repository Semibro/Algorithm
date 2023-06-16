n = int(input())
def rounded(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if n == 0:
    print(0)
else:
    nan2do = [int(input()) for _ in range(n)]
    nan2do.sort()
    cut = rounded(n * 0.15)
    print(rounded(sum(nan2do[0+cut:n-cut])/len(nan2do[0+cut:n-cut])))