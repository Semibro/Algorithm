# def solution(points, routes):
#     N = 0
#     for point in points:
#         N = max(N, point[0], point[1])
        
#     board = [[[] for _ in range(N+1)] for _ in range(N+1)]
        
#     for route in routes:
#         count = 1
#         start_x, start_y = points[route[0]-1][0], points[route[0]-1][1]
#         end_x, end_y = points[route[1]-1][0], points[route[1]-1][1]
#         board[start_x][start_y].append(count)
#         temp_x = -1
        
#         if abs(start_x - end_x) > 0:
#             if start_x - end_x < 0:
#                 for i in range(start_x+1, end_x+1):
#                     count += 1
#                     board[i][start_y].append(count)
#                     temp_x = i
#             else:
#                 for i in range(end_x-1, start_x-1, -1):
#                     count += 1
#                     board[i][start_y].append(count)
#                     temp_x = i
            
#         if abs(start_y - end_y) > 0:
#             if start_y - end_y < 0:
#                 for j in range(start_y+1, end_y+1):
#                     count += 1
#                     board[temp_x][j].append(count)
#             else:
#                 for j in range(end_y-1, start_y-1, -1):
#                     count += 1
#                     board[temp_x][j].append(count)
                    
#     answer = 0
        
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if len(board[i][j]) > 0:
#                 default_len = len(board[i][j])
#                 changed_len = len(set(board[i][j]))
#                 if default_len != changed_len:
#                     answer += 1
                    
#     return answer

###

from collections import defaultdict

def solution(points, routes):
    # 포인트 번호(1~n)를 좌표로 매핑
    point_dict = {i + 1: (r, c) for i, (r, c) in enumerate(points)}
    
    # 시간별 좌표에 도달한 로봇 수를 저장할 딕셔너리
    time_position_map = defaultdict(lambda: defaultdict(int))  # {time: {(r, c): count}}

    for route in routes:
        time = 0
        for i in range(len(route) - 1):
            start = point_dict[route[i]]
            end = point_dict[route[i + 1]]
            r, c = start
            target_r, target_c = end

            # r 좌표 먼저 이동
            while r != target_r:
                time_position_map[time][(r, c)] += 1
                time += 1
                r += 1 if r < target_r else -1

            # c 좌표 이동
            while c != target_c:
                time_position_map[time][(r, c)] += 1
                time += 1
                c += 1 if c < target_c else -1

        # 마지막 도착 지점도 기록
        time_position_map[time][(r, c)] += 1

    # 위험 상황 세기: 같은 좌표에 같은 시간에 로봇 2대 이상이면 위험
    answer = 0
    for time in time_position_map:
        for pos in time_position_map[time]:
            if time_position_map[time][pos] >= 2:
                answer += 1

    return answer