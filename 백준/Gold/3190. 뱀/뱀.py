import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
apple = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    apple.append((x, y))
move = [0] * 10001
for _ in range(int(input())):
    a, b = input().split()
    move[int(a)] = b

# 뱀의 꼬리가 줄어드므로 덱을 이용해 풀이 진행
snake = deque()
snake.appendleft((1, 1))

# 오른쪽(0), 왼쪽(1), 아래쪽(2), 위쪽(3)
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dist = 1  # 처음에는 오른쪽으로 이동
answer = 0

while True:
    answer += 1
    x, y = snake[0][0], snake[0][1]  # 현재 머리
    dx, dy = x+delta[dist][0], y+delta[dist][1]  # 이동한 머리
    if 1<=dx<=N and 1<=dy<=N and (dx, dy) not in snake:  # 벽이거나 뱀이 아닐 때
        snake.appendleft((dx, dy))  # 머리 위치 확장
        if (dx, dy) in apple:  # 사과일 때
            apple.remove((dx, dy))   # 사과 처리
        else:  # 꼬리 땡기기
            snake.pop()
        if move[answer] == 'D':  # 우회전
            dist = (dist+1)%4
        elif move[answer] == 'L':  # 좌회전
            dist = (dist+3)%4
    else:
        break

print(answer)