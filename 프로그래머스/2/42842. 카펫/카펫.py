def solution(brown, yellow):
    for row in range(brown // 2 - 1, 2, -1):
        col = brown // 2 - row + 2
        if (row - 2) * (col - 2) == yellow:
            return [row, col]