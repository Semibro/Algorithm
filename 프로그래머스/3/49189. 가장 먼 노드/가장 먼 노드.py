import heapq

def solution(n, vertex):
    INF = 9876543210
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n + 1)
    
    for a, b in vertex:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
        
    def dijkstra(start):
        heap = []
        
        heapq.heappush(heap, (0, start))
        distance[start] = 0
        
        while heap:
            current_weight, current_node = heapq.heappop(heap)
            
            if distance[current_node] < current_weight:
                continue
                
            for next_node, next_weight in graph[current_node]:
                next_cost = distance[current_node] + next_weight
                
                if next_cost < distance[next_node]:
                    distance[next_node] = next_cost
                    heapq.heappush(heap, (next_cost, next_node))
    
    dijkstra(1)
    
    max_value = 0
    for i in range(1, n+1):
        if distance[i] != INF and distance[i] > max_value:
            max_value = distance[i]
            
    answer = distance.count(max_value)
    
    return answer