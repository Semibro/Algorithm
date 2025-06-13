# 그리디 + 최대 힙

import heapq

def solution(n, k, enemy):
    heap = []
    
    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])
        n -= enemy[i]
        
        if n < 0:
            # 병사로 적을 막되, 병사가 부족해지면 지금까지 가장 많은 적을 무적 처리한다.
            if k > 0:
                largest = -heapq.heappop(heap)
                n += largest
                k -= 1
            else:
                return i
            
    return len(enemy)