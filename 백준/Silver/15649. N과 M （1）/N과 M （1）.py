def backtracking(a):
    if len(a) == M:
        print(' '.join(map(str, a)))
        return
    else:
        for i in range(1, N+1):
            if i not in a:
                a.append(i)
                backtracking(a)
                a.pop()

N, M = map(int, input().split())
lst = []
backtracking(lst)