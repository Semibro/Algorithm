from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [False] * n
    
    for computer in range(n):
        if visited[computer] == False:
            queue.append(computer)
            answer += 1
            while queue:
                temp = queue.popleft()
                for connect in range(n):
                    if temp != connect and computers[temp][connect] == 1 and visited[connect] == False:
                        visited[connect] = True
                        queue.append(connect)
        
    return answer