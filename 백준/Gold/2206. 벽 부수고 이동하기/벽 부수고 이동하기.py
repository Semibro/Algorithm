import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
# 벽을 부쉈는지 파악하기 위해 z축 생성
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
delta = [(1, 0), (0, 1), (0, -1), (-1, 0)]
queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1
# -1 출력을 위한 flag 생성
flag = 0

while queue:
    cx, cy, wall = queue.popleft()
    if cx == N-1 and cy == M-1:  # (N, M) 도착
        flag = 1  # -1출력 방지를 위한 flag 변경
        print(visited[cx][cy][wall])
        break
    else:
        for d in delta:
            dx, dy = cx+d[0], cy+d[1]
            if 0<=dx<N and 0<=dy<M and visited[dx][dy][wall] == 0:  # 델타 이동 후, 방문하지 않은 곳
                if arr[dx][dy] == 0:  # 갈 수 있는 곳이라면 큐에 추가하고, 방문처리
                    queue.append((dx, dy, wall))
                    visited[dx][dy][wall] = visited[cx][cy][wall] + 1
                if wall == 0 and arr[dx][dy] == 1:  # 아직 벽을 안부쉈는데, 벽이라면
                    queue.append((dx, dy, 1))  # 큐에 추가하고
                    visited[dx][dy][1] = visited[cx][cy][wall] + 1  # 벽을 부순거로 처리 후, 방문처리

if not flag:  # flag가 변동이 없다면 -1 출력
    print(-1)