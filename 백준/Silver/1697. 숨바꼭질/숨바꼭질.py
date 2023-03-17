from collections import deque

N, K = map(int, input().split())
arr = [0] * 100001

queue = deque()
queue.append(N)
arr[N] = 1

while arr[K] == 0:
    t = queue.popleft()
    if 2*t <= 100000 and arr[2*t] == 0:
        queue.append(2*t)
        arr[2*t] = arr[t] + 1
    if t+1 <= 100000 and arr[t+1] == 0:
        queue.append(t+1)
        arr[t+1] = arr[t] + 1
    if t-1 >= 0 and arr[t-1] == 0:
        queue.append(t-1)
        arr[t-1] = arr[t] + 1

print(arr[K]-1)