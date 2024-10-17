import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    
    for item in scoville:
        heapq.heappush(heap, item)
        
    if heap[0] >= K:
        return answer
    
    while len(heap) > 1:
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        thr = one + (two * 2)
        
        heapq.heappush(heap, thr)
        answer += 1
        
        if heap[0] >= K:
            return answer
        
    return -1