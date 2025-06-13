from collections import defaultdict

def solution(topping):
    answer = 0
    left = set()
    right = defaultdict(int)
    
    # 토핑의 전체 개수 저장
    for t in topping:
        right[t] += 1
        
    # 토핑 개수 비교
    for i in range(len(topping)):
        left.add(topping[i])
        right[topping[i]] -= 1
        
        if right[topping[i]] == 0:
            del right[topping[i]]
            
        if len(left) == len(right):
            answer += 1
            
    return answer