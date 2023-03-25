from collections import deque

N = int(input())
balloon = list(map(int, input().split()))
queue = deque()
result = []

for i in range(1, N+1):
    queue.append((i, balloon[i-1]))

a = queue.popleft()
result.append(a[0])
idx = a[1]

while queue:
    if idx > 1:
        queue.append(queue.popleft())
        idx -= 1
    elif idx < -1:
        queue.appendleft(queue.pop())
        idx += 1
    elif idx == 1:
        b = queue.popleft()
        result.append(b[0])
        idx = b[1]
    else:
        b = queue.pop()
        result.append(b[0])
        idx = b[1]

print(*result)