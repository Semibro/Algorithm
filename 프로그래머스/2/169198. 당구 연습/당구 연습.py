def distance_sq(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def solution(m, n, startX, startY, balls):
    answer = []
    
    for ballX, ballY in balls:
        min_distance = 9876543210
        candidates = []
        
        # 왼쪽벽
        if not (ballY == startY and ballX < startX):
            candidates.append((-ballX, ballY))
        # 오른쪽벽
        if not (ballY == startY and ballX > startX):
            candidates.append((2 * m - ballX, ballY))
        # 아래쪽벽
        if not (ballX == startX and ballY < startY):
            candidates.append((ballX, -ballY))
        # 위쪽벽
        if not (ballX == startX and ballY > startY):
            candidates.append((ballX, 2 * n - ballY))

        for cx, cy in candidates:
            min_distance = min(min_distance, distance_sq(startX, startY, cx, cy))
        answer.append(min_distance)
        
    return answer