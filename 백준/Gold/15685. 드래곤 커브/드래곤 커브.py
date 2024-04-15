N = int(input())
# 드래곤커브를 체크하기 위한 맵
answer_map = [[0 for _ in range(101)] for _ in range(101)]

# 드래곤 커브 방향은 우 상 좌 하
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

for _ in range(N):
    # x, y는 드래콘커브 시작점 / d는 시작방향 / g는 세대
    sy, sx, d, g = map(int, input().split())
    # 0세대 위치좌표 설정
    lst = [(sx, sy), (sx+di[d], sy+dj[d])]

    for _ in range(g):
        # lst의 끝좌표를 기준으로 90도 회전
        ex, ey = lst[-1] # 끝좌표
        for i in range(len(lst)-2, -1, -1):
            cx, cy = lst[i]
            lst.append((ex-(ey-cy), ey+(ex-cx)))

    # 맵에 표시
    for i, j in lst:
        answer_map[i][j] = 1

# count찾기
# 정답을 카운트하기 위한 변수
answer_count = 0

for i in range(100):
    for j in range(100):
        if answer_map[i][j] == answer_map[i+1][j] == answer_map[i][j+1] == answer_map[i+1][j+1] == 1:
            answer_count += 1

print(answer_count)