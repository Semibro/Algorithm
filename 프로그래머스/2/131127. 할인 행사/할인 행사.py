from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    def check(discount_dict):
        for i in range(len(want)):
            if discount_dict[want[i]] and discount_dict[want[i]] >= number[i]:
                continue
            else:
                return False
        return True
    
    discount_dictionary = defaultdict(int)
    
    for i in range(10):
        discount_dictionary[discount[i]] += 1
        
    if len(discount) == 10:
        if check(discount_dictionary):
            return 1
        else:
            return 0
    else:
        if check(discount_dictionary):
            answer += 1
        
    for i in range(10, len(discount)):
        discount_dictionary[discount[i-10]] -= 1
        if discount_dictionary[discount[i-10]] == 0:
            del discount_dictionary[discount[i-10]]
        discount_dictionary[discount[i]] += 1
        
        if check(discount_dictionary):
            answer += 1
            
    return answer