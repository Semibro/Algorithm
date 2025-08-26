def solution(n, times):
    answer = 0
    left, right = 1, n * max(times)
    
    while left <= right:
        mid = (left + right) // 2
        
        people_count = 0  # mid 시간 동안 처리할 수 있는 사람의 수
        for time in times:
            people_count += mid // time
            
            if people_count >= n:
                break
                
        if people_count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer