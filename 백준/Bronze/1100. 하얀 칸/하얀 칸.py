chess = [['.']*8 for _ in range(8)] # 빈 체스판 생성
board = [input() for _ in range(8)] # 체스판 input
count = 0 # 말이 올려진 칸을 세기 위한 count

for i in range(0, 8):
    if i % 2 == 0: # 짝수 행은 0 2 4 6이 하얀 칸
        for j in range(0, 7, 2):
            if chess[i][j] != board[i][j]: # 하얀칸에 다른게 들어있으면 +1
                count += 1
    else: # 홀수 행은 1 3 5 7이 하얀 칸
        for j in range(1, 8, 2):
            if chess[i][j] != board[i][j]: # 하얀칸에 다른게 들어있으면 +1
                count += 1

print(count)