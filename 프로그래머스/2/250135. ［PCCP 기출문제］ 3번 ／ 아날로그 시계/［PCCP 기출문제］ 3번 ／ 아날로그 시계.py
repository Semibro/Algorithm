def solution(h1, m1, s1, h2, m2, s2):
    alarm = 0
    
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2
    
    # next 각도를 기준으로 체크하므로, 포함되지 않는 시간 카운트 (0시, 12시)
    if start_time == 0 or start_time == 3600 * 12:
        alarm += 1
    
    while start_time < end_time:
        # 현재 시침, 분침, 초침의 각도 구하기
        current_hour_angle = start_time / 120 % 360
        current_minute_angle = start_time / 10 % 360
        current_second_angle = start_time * 6 % 360
        
        # 다음 시침, 분침, 초침의 각도 구하기
        next_hour_angle = 360 if (start_time + 1) / 120 % 360 == 0 else (start_time + 1) / 120 % 360
        next_minute_angle = 360 if (start_time + 1) / 10 % 360 == 0 else (start_time + 1) / 10 % 360
        next_second_angle = 360 if (start_time + 1) * 6 % 360 == 0 else (start_time + 1) * 6 % 360
        
        # 초침이 시침이나 분침을 지나갔는지 확인
        if current_second_angle < current_hour_angle and next_second_angle >= next_hour_angle:
            alarm += 1
        if current_second_angle < current_minute_angle and next_second_angle >= next_minute_angle:
            alarm += 1
            
        # 동시에 겹친 상황을 제외
        if next_second_angle == next_minute_angle and next_second_angle == next_hour_angle:
            alarm -= 1
            
        start_time += 1
        
    return alarm