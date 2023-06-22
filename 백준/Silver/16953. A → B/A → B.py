A, B = map(int, input().split())
answer = 0

def bt(n, cnt):
    global answer
    if n > B:
        return
    if n == B:
        answer = cnt
        return
    else:
        bt(n*2, cnt+1)
        bt(int(str(n)+'1'), cnt+1)

bt(A, 0)
if answer:
    print(answer+1)
else:
    print(-1)