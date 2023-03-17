from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    heap_max = []
    heap_min = []
    visited = [False] * k
    for i in range(k):
        a, b = input().split()
        if a == 'I':
            heappush(heap_min, (int(b), i))
            heappush(heap_max, (-int(b), i))
            visited[i] = True
        else:
            if b == '-1':
                while len(heap_min) > 0 and not visited[heap_min[0][1]]:
                    heappop(heap_min)
                if len(heap_min) > 0:
                    visited[heap_min[0][1]] = False
                    heappop(heap_min)
            else:
                while len(heap_max) > 0 and not visited[heap_max[0][1]]:
                    heappop(heap_max)
                if len(heap_max) > 0:
                    visited[heap_max[0][1]] = False
                    heappop(heap_max)

    while len(heap_min) > 0 and not visited[heap_min[0][1]]:
        heappop(heap_min)
    while len(heap_max) > 0 and not visited[heap_max[0][1]]:
        heappop(heap_max)

    if len(heap_min) == 0 and len(heap_max) == 0:
        print('EMPTY')
    else:
        print(-heap_max[0][0], heap_min[0][0])