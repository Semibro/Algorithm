import heapq

def solution(n, paths, gates, summits):
    INF = 9876543210
    graph = [[] for _ in range(n+1)]
    
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    def dijkstra():
        heap = []
        distance = [INF] * (n+1)
        
        for gate in gates:
            heapq.heappush(heap, (0, gate))
            distance[gate] = 0
            
        while heap:
            current_intensity, current_node = heapq.heappop(heap)
            
            if distance[current_node] < current_intensity or current_node in summits:
                continue
            
            for next_node, next_intensity in graph[current_node]:
                cost_intensity = max(current_intensity, next_intensity)
                
                if cost_intensity < distance[next_node]:
                    distance[next_node] = cost_intensity
                    heapq.heappush(heap, (cost_intensity, next_node))
                    
        return distance
    
    res_dist = dijkstra()
    
    summits.sort()

    row_index, row_intensity = -1, INF

    for summit in summits:
        if res_dist[summit] < row_intensity:
            row_intensity = res_dist[summit]
            row_index = summit
            
    return [row_index, row_intensity]