t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    if N == 1:
        print(1)
    else:
        queue = []
        for i in range(N):
            queue.append(i)
        cnt = 0
        while True:
            if queue[0] == M and imp[0] == max(imp):
                print(cnt+1)
                break
            else:
                if imp[0] == max(imp):
                    imp.pop(0)
                    queue.pop(0)
                    cnt += 1
                else:
                    i = imp.pop(0)
                    imp.append(i)
                    q = queue.pop(0)
                    queue.append(q)