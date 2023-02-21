import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

N = int(input())
for _ in range(N):
    command = list(map(str, input().split()))
    if command[0] == 'push_front':
        queue.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        queue.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])