def solution(n, lost, reserve):
    # 체육복을 도난당한 학생들의 번호 - lost
    # 여벌의 체육복을 가져온 학생들의 번호 - reserve
    
    answer = 0  # 체육 수업을 들을 수 있는 학생 수의 최댓값
    clothes = [1 for _ in range(n+1)]  # 0~n
    
    # lost
    for student in lost:
        clothes[student] -= 1
        
    # reserve
    for student in reserve:
        clothes[student] += 1
        
    # calc answer
    for idx in range(1, n+1):
        if clothes[idx] == 1:
            answer += 1
        elif clothes[idx] == 0:
            if idx-1 > 0 and clothes[idx-1] == 2:
                clothes[idx-1] -= 1
                clothes[idx] += 1
                answer += 1
            elif idx+1 < n+1 and clothes[idx+1] == 2:
                clothes[idx+1] -= 1
                clothes[idx] += 1
                answer += 1
        else:
            answer += 1
    
    return answer