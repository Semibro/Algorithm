N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
# 왼족 아래 오른쪽 위 순으로 움직임
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
sand_patterns = {
    0: [  # 좌
        (-1, 1, 0.01), (-1, 0, 0.07), (-2, 0, 0.02),
        (-1, -1, 0.1), (0, -2, 0.05), (1, -1, 0.1),
        (1, 0, 0.07), (2, 0, 0.02), (1, 1, 0.01)
    ],
    1: [  # 하
        (-1, -1, 0.01), (0, -1, 0.07), (0, -2, 0.02),
        (1, -1, 0.1), (2, 0, 0.05), (1, 1, 0.1),
        (0, 1, 0.07), (0, 2, 0.02), (-1, 1, 0.01)
    ],
    2: [  # 우
        (-1, -1, 0.01), (-1, 0, 0.07), (-2, 0, 0.02),
        (-1, 1, 0.1), (0, 2, 0.05), (1, 1, 0.1),
        (1, 0, 0.07), (2, 0, 0.02), (1, -1, 0.01)
    ],
    3: [  # 상
        (1, -1, 0.01), (0, -1, 0.07), (0, -2, 0.02),
        (-1, -1, 0.1), (-2, 0, 0.05), (-1, 1, 0.1),
        (0, 1, 0.07), (0, 2, 0.02), (1, 1, 0.01)
    ]
}
sx, sy = N // 2, N // 2
answer = 0

def spread_sand(cx, cy, dir):
    global answer

    total_sand = A[cx][cy]
    A[cx][cy] = 0
    sand_sum = 0

    for dx, dy, ratio in sand_patterns[dir]:
        nx, ny = cx + dx, cy + dy
        sand = int(total_sand * ratio)
        sand_sum += sand

        if 0 <= nx < N and 0 <= ny < N:
            A[nx][ny] += sand
        else:
            answer += sand

    ax, ay = cx + direction[dir][0], cy + direction[dir][1]
    remain_sand = total_sand - sand_sum
    if 0 <= ax < N and 0 <= ay < N:
        A[ax][ay] += remain_sand
    else:
        answer += remain_sand

direction_index = 0
length = 1

while True:
    for _ in range(2):
        for _ in range(length):
            sx += direction[direction_index][0]
            sy += direction[direction_index][1]

            if A[sx][sy] > 0:
                spread_sand(sx, sy, direction_index)

            if sx == 0 and sy == 0:
                print(answer)
                exit()
        direction_index = (direction_index + 1) % 4
    length += 1