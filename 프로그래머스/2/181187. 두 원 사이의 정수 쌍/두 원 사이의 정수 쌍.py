import math

def solution(r1, r2):
    answer = 0
    
    for x in range(1, r2+1):
        maxH = math.floor(math.sqrt(r2**2 - x**2))
        
        if x >= r1:
            minH = 0
        else:
            minH = math.ceil(math.sqrt(r1**2 - x**2))
        
        answer += (maxH - minH + 1)
        
    return answer * 4