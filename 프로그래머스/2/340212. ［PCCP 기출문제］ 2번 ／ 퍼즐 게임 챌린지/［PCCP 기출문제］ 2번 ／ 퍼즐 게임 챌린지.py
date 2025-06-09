def solution(diffs, times, limit):
    def solve_puzzle(level):
        time = 0
        
        for idx in range(len(diffs)):
            if diffs[idx] > level:
                wrong_count = diffs[idx] - level
                time_prev = 0 if idx == 0 else times[idx-1]
                time += wrong_count * (times[idx] + time_prev)
            time += times[idx]
            
            if time > limit:
                return False
        
        return time <= limit
    
    left, right = 1, max(diffs)
    
    while left <= right:
        mid = (left + right) // 2
        
        if solve_puzzle(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left
            