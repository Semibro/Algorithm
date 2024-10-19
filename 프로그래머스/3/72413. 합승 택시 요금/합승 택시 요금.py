# n = 지점의 개수
# s = 출발지점
# a = A의 도착지점
# b = B의 도착지점

import heapq

def solution(n, s, a, b, fares):
    INF = 9876543210
    graph = [[] for _ in range(n+1)]
    
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
        
    def dijkstra(start, end):
        # 세팅
        distance = [INF for _ in range(n+1)]
        heap = []
        
        # 초기화
        distance[start] = 0
        heapq.heappush(heap, (0, start))
        
        # 다익스트라
        while heap:
            dist, nowNode = heapq.heappop(heap)
            
            for nextNode, fee in graph[nowNode]:
                cost = distance[nowNode] + fee
                
                if cost < distance[nextNode]:
                    distance[nextNode] = cost
                    heapq.heappush(heap, (cost, nextNode))
        
        return distance[end]
    
    # 1. s에서 시작해서 a, b 각각 거리 더하기
    # 2. s에서 a까지 거리 b까지 거리 구하고
    #    a에서 b까지, b에서 a까지 거리 더하기
    
    answer = 9876543210
    for idx in range(1, n+1):
        answer = min(answer, dijkstra(s, idx)+dijkstra(idx, a)+dijkstra(idx, b))
        
    return answer