import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [[9]+[0]*N+[9] for _ in range(N)]
board = [[9]*(N+2)] + board + [[9]*(N+2)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x][y] = 1
move = ['.'] * 10001
for _ in range(int(input())):
    X, D = input().split()
    move[int(X)] = D

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
    if board[dx][dy] != 9 and (dx, dy) not in snake:  # 벽이거나 뱀이 아닐 때
        snake.appendleft((dx, dy))  # 머리 위치 확장
        if board[dx][dy] == 1:  # 사과일 때
            board[dx][dy] = 0   # 사과 처리
        else:  # 꼬리 땡기기
            snake.pop()
        if move[answer] == 'D':  # 우회전
            dist = (dist+1)%4
        elif move[answer] == 'L':  # 좌회전
            dist = (dist+3)%4
    else:
        break

print(answer)