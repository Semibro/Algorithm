def solution(storey):
    answer = float('inf')
    
    def bt(storey, count):  
        nonlocal answer
        
        # 가지치기
        if count >= answer:
            return
        
        if storey == 0:
            answer = min(answer, count)
            return
        
        # 자릿수 처리
        digit = storey % 10
        remain = storey // 10
        
        bt(remain, count + digit)
        bt(remain + 1, count + (10 - digit))
        
    bt(storey, 0)
    
    return answer