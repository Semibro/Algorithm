import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = [0] * N  # N-1위치에서 로봇 내림

zero_cnt = 0
answer = 0

while True:
    answer += 1

    # [1] 벨트 이동, 로봇 회전 / 로봇 내림
    belt.appendleft(belt.pop())
    robot = [0] + robot[:-1]
    robot[N-1] = 0

    # [2] 로봇여부 판단, 로봇 우측이동
    for i in range(N-2, 0, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
            robot[i], robot[i+1] = 0, 1
            belt[i+1] -= 1
            if belt[i+1] == 0:
                zero_cnt += 1

    # [3] 로봇 올리기
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            zero_cnt += 1

    # [4] 0개수 판단
    if zero_cnt >= K:
        break

print(answer)