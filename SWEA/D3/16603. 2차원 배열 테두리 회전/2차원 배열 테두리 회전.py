from collections import deque
for _ in range(int(input())):
    queue = deque()
    tc = int(input())
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [[0]*M for _ in range(N)]
    bin_lst = []
    for i in range(N):
        if i == 0:
            for j in range(M):
                queue.append(arr[i][j])
        elif i == N-1:
            for j in range(M-1, -1, -1):
                queue.append(arr[i][j])
        else:
            bin_lst.append(arr[i][0])
            queue.append(arr[i][-1])
    for i in range(len(bin_lst)-1, -1, -1):
        queue.append(bin_lst[i])
    idx = 0
    while idx != K:
        idx += 1
        queue.appendleft(queue.pop())
    idx1 = 0
    for i in range(N):
        if i == 0:
            for j in range(M):
                result[i][j] = queue[idx1]
                idx1 += 1
        elif i == N-1:
            for j in range(M-1, -1, -1):
                result[i][j] = queue[idx1]
                idx1 += 1
        else:
            result[i][-1] = queue[idx1]
            idx1 += 1
    for i in range(N-2, 0, -1):
        result[i][0] = queue[idx1]
        idx1 += 1
    for i in range(1, N-1):
        for j in range(1, M-1):
            result[i][j] = arr[i][j]

    print(f'#{tc}')
    for i in result:
        print(*i)