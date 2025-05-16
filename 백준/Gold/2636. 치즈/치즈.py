import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    queue = deque()
    visited = [[False] * M for _ in range(N)]
    queue.append((0, 0))
    visited[0][0] = True
    melting_cheese = []
    
    while queue:
        current_x, current_y = queue.popleft()
        
        for direction_x, direction_y in direction:
            next_x = current_x + direction_x
            next_y = current_y + direction_y
            
            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= M:
                continue;
            
            if visited[next_x][next_y]:
                continue;
                
            visited[next_x][next_y] = True
            
            if cheese[next_x][next_y] == 1:
                melting_cheese.append((next_x, next_y))
            else:
                queue.append((next_x, next_y))
    
    for x, y in melting_cheese:
        cheese[x][y] = 0
    
    return len(melting_cheese)

time = 0
cheese_count = 0

while True:
    melted_cheese_count = bfs()
    
    if melted_cheese_count == 0:
        break
    else:
        time += 1
        cheese_count = melted_cheese_count
        
print(time)
print(cheese_count)