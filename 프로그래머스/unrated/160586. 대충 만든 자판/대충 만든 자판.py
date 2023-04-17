def solution(keymap, targets):
    answer = []
    for target in targets:  # ABCD
        res = 0
        for tar in target:  # A
            min_v = 9876543210
            for key in keymap:  # ABACD
                if tar in key:
                    min_v = min(min_v, key.index(tar)+1)
            res += min_v
        if res >= 9876543210:
            answer.append(-1)
        else:
            answer.append(res)
        
    return answer