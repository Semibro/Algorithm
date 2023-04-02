k = int(input())
lst = list(input().split())
visited = [0] * 10
max_v, min_v = '0', '9876543210'

def bt(n, res, idx):
    global max_v, min_v
    if n == k+1:
        imsi = ''
        for i in res:
            imsi += str(i)
        if int(max_v) < int(imsi):
            max_v = imsi
        if int(min_v) > int(imsi):
            min_v = imsi
        return
    else:
        for i in range(10):
            if not visited[i]:
                visited[i] = 1
                if idx == 0:
                    res.append(i)
                    bt(n+1, res, idx+1)
                    res.pop()
                else:
                    if lst[idx-1] == '>':
                        if res[-1] > i:
                            res.append(i)
                            bt(n+1, res, idx+1)
                            res.pop()
                    else:
                        if res[-1] < i:
                            res.append(i)
                            bt(n+1, res, idx+1)
                            res.pop()
                visited[i] = 0

bt(0, [], 0)
print(max_v)
print(min_v)