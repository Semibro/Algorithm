def change_time(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def solution(plans):
    answer = []
    pause_work = []
    N = len(plans)
    
    # 시작시간을 분 형태로 변경하여 정렬
    for index in range(N):
        plans[index][1] = change_time(plans[index][1])
        plans[index][2] = int(plans[index][2])
    plans.sort(key = lambda x: x[1])
    
    # 과제 진행
    for index in range(N-1):
        name, start, playtime = plans[index]
        next_start = plans[index + 1][1]
        end_time = start + playtime
        
        if end_time <= next_start:
            answer.append(name)
            spare_time = next_start - end_time
            
            while pause_work and spare_time > 0:
                prev_name, remain_time = pause_work.pop()
                
                if remain_time <= spare_time:
                    answer.append(prev_name)
                    spare_time -= remain_time
                else:
                    pause_work.append((prev_name, remain_time - spare_time))
                    break
        else:
            remain_time = end_time - next_start
            pause_work.append((name, remain_time))
    
    # 마지막 과제 처리
    answer.append(plans[-1][0])
    
    # 멈춘 과제 처리
    while pause_work:
        answer.append(pause_work.pop()[0])
        
    return answer