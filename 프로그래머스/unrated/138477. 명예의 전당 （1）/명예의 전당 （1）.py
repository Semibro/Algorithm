from heapq import heappush, heappop

def solution(k, score):
    answer = []
    heap = []
    for s in score:
        if len(heap) < k:
            heappush(heap, s)
            answer.append(heap[0])
        else:
            if heap[0] <= s:
                heappop(heap)
                heappush(heap, s)
                answer.append(heap[0])
            else:
                answer.append(heap[0])
    return answer