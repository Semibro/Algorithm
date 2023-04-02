N = int(input())
lst = list(map(int, input().split()))
k = int(input())
result = []

def divideandconquer(n, lst, lst2):
    global result
    if n == k:
        print(*lst[:])
        return
    else:
        m = n//2
        for i in range(0, N, N//m):
            lst3 = lst[i:i+N//m]
            lst3.sort()
            lst2.extend(lst3)
        divideandconquer(m, lst2, [])

divideandconquer(N, lst, [])