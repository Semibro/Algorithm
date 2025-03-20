def solution(clothes):
    answer = 1
    items = {}
    
    for c in clothes:
        if c[1] in items:
            items[c[1]] += 1
        else:
            items[c[1]] = 1
    
    for v in items.values():
        answer *= v + 1
    
    return answer - 1