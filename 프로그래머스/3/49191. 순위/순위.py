def solution(n, results):
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for A, B in results:
        graph[A][B] = True
        
    # 플로이드-워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
                    
    answer = 0
    for idx in range(1, n + 1):
        win, lose = 0, 0
        
        for jdx in range(1, n + 1):
            if graph[idx][jdx]:
                win += 1
            if graph[jdx][idx]:
                lose += 1
                
        if win + lose == n - 1:
            answer += 1
            
    return answer