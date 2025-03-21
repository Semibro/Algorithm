from collections import deque

def bfs(start_node, graph, node_count):
    visited = [False] * (node_count + 1)
    queue = deque()
    visited[start_node] = True
    queue.append(start_node)
    count = 1
    
    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if not visited[next_node]:
                count += 1
                visited[next_node] = True
                queue.append(next_node)
                
    return count

def solution(n, wires):
    answer = n
    
    for idx in range(len(wires)):
        temp = wires[:idx] + wires[idx+1:]
        
        graph = [[] for _ in range(n+1)]
        for u, v in temp:
            graph[u].append(v)
            graph[v].append(u)
            
        count = bfs(1, graph, n)
        other_count = n - count
        
        answer = min(answer, abs(count - other_count))
        
    return answer