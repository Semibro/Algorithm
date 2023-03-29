import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    queue = deque()
    visited = [''] * 10000
    queue.append(A)
    visited[A] += 'Z'
    while queue:
        t = queue.popleft()

        D = (t*2) % 10000
        if visited[D] == '':
            queue.append(D)
            visited[D] += visited[t] + 'D'
            if D == B:
                print(visited[D][1:])
                break

        S = (t-1) % 10000
        if visited[S] == '':
            queue.append(S)
            visited[S] += visited[t] + 'S'
            if S == B:
                print(visited[S][1:])
                break

        L = (t*10 + (t//1000)) % 10000
        if visited[L] == '':
            queue.append(L)
            visited[L] += visited[t] + 'L'
            if L == B:
                print(visited[L][1:])
                break

        R = (t//10 + (t%10) * 1000) % 10000
        if visited[R] == '':
            queue.append(R)
            visited[R] += visited[t] + 'R'
            if R == B:
                print(visited[R][1:])
                break