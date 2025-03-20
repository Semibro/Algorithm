def solution(k, dungeons):
    N = len(dungeons)
    count = 0
    
    def dfs(p, visited, c):
        nonlocal count
        count = max(count, c)
        
        for idx in range(N):
            if not visited[idx] and p >= dungeons[idx][0]:
                visited[idx] = True
                dfs(p-dungeons[idx][1], visited, c+1)
                visited[idx] = False
                
    visited = [False] * N
    dfs(k, visited, 0)
    
    return count