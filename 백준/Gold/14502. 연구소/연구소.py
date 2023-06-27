from collections import deque
import copy, sys
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0

def bfs(n):
    global answer
    if n == 3:
        temp_lab = copy.deepcopy(lab)
        queue = deque()
        for i in range(N):
            for j in range(M):
                if temp_lab[i][j] == 2:
                    queue.append((i, j))
        while queue:
            cx, cy = queue.popleft()
            for d in delta:
                dx, dy = cx+d[0], cy+d[1]
                if 0<=dx<N and 0<=dy<M and temp_lab[dx][dy] == 0:
                    temp_lab[dx][dy] = 2
                    queue.append((dx, dy))
        # 0의 개수 세기
        cnt = 0
        for x in range(N):
            for y in range(M):
                if temp_lab[x][y] == 0:
                    cnt += 1
        answer = max(answer, cnt)
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                bfs(n+1)
                lab[i][j] = 0

bfs(0)
print(answer)