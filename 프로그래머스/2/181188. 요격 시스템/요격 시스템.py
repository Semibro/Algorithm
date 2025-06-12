def solution(targets):
    sorted_targets = sorted(targets, key = lambda x: x[1])
    
    missile, end = 0, 0
    for s, e in sorted_targets:
        if s >= end:
            missile += 1
            end = e
            
    return missile