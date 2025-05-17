import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magic = [list(map(int, input().split())) for _ in range(M)]
direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
shark_x, shark_y = N // 2, N // 2

# 나선형 경로 생성
def create_spiral_path():
    path = []
    x, y = shark_x, shark_y
    length = 1
    dxs = [0, 1, 0, -1]
    dys = [-1, 0, 1, 0]
    dir_idx = 0

    while True:
        for _ in range(2):
            dx, dy = dxs[dir_idx], dys[dir_idx]
            for _ in range(length):
                x += dx
                y += dy
                if x < 0 or y < 0 or x >= N or y >= N:
                    return path
                path.append((x, y))
            dir_idx = (dir_idx + 1) % 4
        length += 1

spiral = create_spiral_path()
total_score = [0, 0, 0, 0]

# 구슬 파괴
def destroy_magic(dir, step):
    dx, dy = direction[dir]
    for i in range(1, step + 1):
        nx = shark_x + dx * i
        ny = shark_y + dy * i
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] = 0

# 구슬 추출
def extract_beads():
    beads = []
    for x, y in spiral:
        if board[x][y] != 0:
            beads.append(board[x][y])
    return beads

# 구슬 폭발
def explode(beads):
    global total_score
    while True:
        new_beads = []
        exploded = False
        idx = 0

        while idx < len(beads):
            jdx = idx
            while jdx < len(beads) and beads[idx] == beads[jdx]:
                jdx += 1

            count = jdx - idx
            if count >= 4:
                total_score[beads[idx]] += count
                exploded = True
            else:
                new_beads.extend(beads[idx:jdx])

            idx = jdx

        if not exploded:
            break
        beads = new_beads

    return beads

# 구슬 변환
def transform(beads):
    new_beads = []
    idx = 0
    while idx < len(beads):
        jdx = idx
        while jdx < len(beads) and beads[idx] == beads[jdx]:
            jdx += 1

        count = jdx - idx
        new_beads.append(count)
        new_beads.append(beads[idx])
        idx = jdx

        if len(new_beads) >= len(spiral):
            break

    return new_beads[:len(spiral)]

# 구슬 다시 보드에 채우기
def fill_beads(beads):
    for idx, (x, y) in enumerate(spiral):
        if idx < len(beads):
            board[x][y] = beads[idx]
        else:
            board[x][y] = 0

# 전체 시뮬레이션
for d, s in magic:
    destroy_magic(d, s)
    beads = extract_beads()
    beads = explode(beads)
    beads = transform(beads)
    fill_beads(beads)

print(total_score[1] + total_score[2] * 2 + total_score[3] * 3)