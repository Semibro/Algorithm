import math
from collections import defaultdict

def solution(fees, records):
    in_time_dict = defaultdict(int)
    record_dict = defaultdict(int)
    answer_dict = defaultdict(int)
    last_time = 60 * 23 + 59
    
    # 주차 시간 계산
    for record in records:
        time, car_number, rec = record.split(" ")
        hour, minute = time.split(":")
        changed_time = 60 * int(hour) + int(minute)
        
        if rec == "IN":
            in_time_dict[car_number] = changed_time
        else:
            record_dict[car_number] += changed_time - in_time_dict[car_number]
            del in_time_dict[car_number]
            
    if in_time_dict:
        for key in in_time_dict.keys():
            record_dict[key] += last_time - in_time_dict[key]
            
    # 시간에 맞게 요금 계산
    for key in record_dict.keys():
        if record_dict[key] > fees[0]:
            over_time = record_dict[key] - fees[0]
            over_fee = math.ceil(over_time / fees[2])
            answer_dict[key] += over_fee * fees[3]
            
        answer_dict[key] += fees[1]
        
    answer = []
    for key in sorted(answer_dict.keys(), key = lambda x: int(x)):
        answer.append(answer_dict[key])
        
    return answer