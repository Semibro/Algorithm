from collections import deque

N, K = map(int, input().split())
bfs = [0] * 100001
queue = deque()
bfs[N] = 1
queue.append(N)
while queue:
    current = queue.popleft()
    if current == K:
        print(bfs[K]-1)
        break
    if 0<=current-1<=100000 and bfs[current-1] == 0:
        bfs[current-1] = bfs[current] + 1
        queue.append(current-1)
    if 0<=current*2<=100000 and bfs[current*2] == 0:
        bfs[current*2] = bfs[current]
        queue.appendleft(current*2)
    if 0 <= current + 1 <= 100000 and bfs[current + 1] == 0:
        bfs[current + 1] = bfs[current] + 1
        queue.append(current + 1)