import heapq

N = int(input())
heap = []

for _ in range(N):
    temp_list = list(map(int, input().split()))

    if heap:
        for item in temp_list:
            if item > heap[0]:
                heapq.heappush(heap, item)
                heapq.heappop(heap)
    else:
        for item in temp_list:
            heapq.heappush(heap, item)

print(heap[0])