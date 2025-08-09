import heapq

def solution(n, roads, sources, destination):
    INF = 9876543210
    answer = []
    graph = [[] for _ in range(n+1)]
    
    for a, b in roads:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
        
    def dijkstra(start):
        heap = []
        distance = [INF] * (n + 1)
        
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
                    
        return distance
            
    res_list = dijkstra(destination)
    
    for source in sources:
        if res_list[source] == INF:
            answer.append(-1)
        else:
            answer.append(res_list[source])
    
    return answer