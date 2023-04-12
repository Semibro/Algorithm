from collections import deque

def solution(x, y, n):
    visited = [0] * 1000001
    queue = deque()
    queue.append(x)
    visited[x] = 1
    
    while queue:
        t = queue.popleft()
        if t+n <= 1000000 and (not visited[t+n] or visited[t]+1 < visited[t+n]):
            visited[t+n] = visited[t] + 1
            queue.append(t+n)
        if t*2 <= 1000000 and (not visited[t*2] or visited[t]+1 < visited[t*2]):
            visited[t*2] = visited[t] + 1
            queue.append(t*2)
        if t*3 <= 1000000 and (not visited[t*3] or visited[t]+1 < visited[t*3]):
            visited[t*3] = visited[t] + 1
            queue.append(t*3)
    return visited[y]-1