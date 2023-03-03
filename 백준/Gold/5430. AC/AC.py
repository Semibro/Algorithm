from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    lst = deque(input().rstrip()[1:-1].split(','))
    switch = 0
    cnt = 0

    if n == 0:
        lst = deque()

    for j in p:
        if j == 'R':
            cnt += 1
        else:
            if len(lst) <= 0:
                switch = 1
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()

    if switch == 0:
        if cnt % 2 == 0:
            print('[' + ','.join(lst) + ']')
        else:
            lst.reverse()
            print('[' + ','.join(lst) + ']')