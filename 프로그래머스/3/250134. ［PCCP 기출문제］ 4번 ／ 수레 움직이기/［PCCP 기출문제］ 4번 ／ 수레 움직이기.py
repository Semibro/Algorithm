# 0: 빈칸 / 1: 빨간 수레 시작 칸 / 2: 파란 수레 시작 칸 / 3: 빨간 수레 도착 칸 / 4: 파란 수레 도착 칸 / 5: 벽

from collections import deque

def solution(maze):
    N, M = len(maze), len(maze[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 빨간, 파란 수레 시작/도착 지점 찾기
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_end = (i, j)
            elif maze[i][j] == 4:
                blue_end = (i, j)
                
    # 방문 상태 관리
    visited = set()
    queue = deque()
    
    queue.append((red_start, blue_start, frozenset([red_start]), frozenset([blue_start]), 0))
    visited.add((red_start, blue_start, frozenset([red_start]), frozenset([blue_start])))
    
    def get_next(pos, visited_set, end_pos):
        if pos == end_pos:
            return [pos]
        moves = []
        for dx, dy in direction:
            nx, ny = pos[0] + dx, pos[1] + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != 5 and (nx, ny) not in visited_set:
                moves.append((nx, ny))
        return moves
        
    # BFS
    while queue:
        red, blue, red_visited, blue_visited, time = queue.popleft()
        
        # 수레 도착
        if red == red_end and blue == blue_end:
            return time
        
        red_moves = get_next(red, red_visited, red_end)
        blue_moves = get_next(blue, blue_visited, blue_end)
                
        # 수레 이동
        for nr in red_moves:
            for nb in blue_moves:
                # 같은 칸 이동 체크
                if nr == nb:
                    continue
                # 자리 바꾸기 체크
                if red == nb and blue == nr:
                    continue
                    
                new_red_visited = red_visited | {nr}
                new_blue_visited = blue_visited | {nb}
                
                state = (nr, nb, frozenset(new_red_visited), frozenset(new_blue_visited))
                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nb, new_red_visited, new_blue_visited, time + 1))
                    
    return 0