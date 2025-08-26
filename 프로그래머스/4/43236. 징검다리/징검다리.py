def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    answer = 0
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        
        remove_rock_count, pos = 0, 0
        for rock in rocks:
            if rock - pos < mid:
                remove_rock_count += 1
            else:
                pos = rock
            
            if remove_rock_count > n:
                break
                
        if remove_rock_count > n:
            right = mid - 1
        else:
            print(mid)
            answer = mid
            left = mid + 1
            
    return answer