# 중간값 구하기 알고리즘
# 최대 힙의 크기는 최소 힙의 크기와 같거나 하나 더 크다.
# 최대 힙의 최대 원소는 최소 힙의 최소 원소보다 작거나 같다.
# 이 때, 로직에 맞지 않다면 최대 힙, 최소 힙의 가장 위의 값을 swap한다.

import sys
import heapq

input = sys.stdin.readline

max_heap = [] # 최대 힙
min_heap = [] # 최소 힙

def findMid(num):
    # push
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    # swap
    if len(max_heap) != 0 and len(min_heap) != 0 and -max_heap[0] > min_heap[0]:
        temp_max = heapq.heappop(max_heap)
        temp_min = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -temp_min)
        heapq.heappush(min_heap, -temp_max)

    # print
    return -max_heap[0]


N = int(input())
for _ in range(N):
    print(findMid(int(input())))