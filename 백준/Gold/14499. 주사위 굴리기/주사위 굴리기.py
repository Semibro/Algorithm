import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

# 주사위 면 (초기값은 모두 0이다.)
n1 = n2 = n3 = n4 = n5 = n6 = 0
# 방향 이동은 동, 서, 북, 남 (1, 2, 3, 4로 주어지므로 0은 제외)
delta = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

# 명령 방향대로 이동
for direct in lst:
    # 1. 이동 후 범위내이면 처리
    dx, dy = x+delta[direct][0], y+delta[direct][1]
    if 0<=dx<N and 0<=dy<M:
        # 2. 주사위 굴리기
        if direct == 1:  # 동쪽
            n1, n3, n4, n6 = n4, n1, n6, n3
        elif direct == 2:  # 서쪽
            n1, n3, n4, n6 = n3, n6, n1, n4
        elif direct == 3:  # 북쪽
            n1, n2, n5, n6 = n5, n1, n6, n2
        else:  # 남쪽
            n1, n2, n5, n6 = n2, n6, n1, n5

        # 3. 이동한 바닥면이 0인지 판단
        if arr[dx][dy] == 0:
            arr[dx][dy] = n6
        else:
            n6 = arr[dx][dy]
            arr[dx][dy] = 0

        # 4. 이동
        x, y = dx, dy

        print(n1)