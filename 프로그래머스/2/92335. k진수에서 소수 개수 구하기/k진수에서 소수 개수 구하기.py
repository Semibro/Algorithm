def change_number_system(num, ns):
    if num == 0:
        return "0"
    
    digits = []
    while num > 0:
        digits.append(str(num % ns))
        num //= ns
    return "".join(reversed(digits))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    changed_number = change_number_system(n, k)
    
    if "0" in changed_number:
        answer, index = 0, 0
        temp_str, res = "", []
        
        while index < len(changed_number):
            if changed_number[index] == "0":
                if len(temp_str) > 0:
                    res.append(int(temp_str))
                    temp_str = ""
            else:
                temp_str += changed_number[index]
            index += 1
        
        if len(temp_str) > 0:
            res.append(int(temp_str))
            
        for r in res:
            if is_prime(r):
                answer += 1
                
        return answer
    else:
        if is_prime(int(changed_number)):
            return 1
        else:
            return 0