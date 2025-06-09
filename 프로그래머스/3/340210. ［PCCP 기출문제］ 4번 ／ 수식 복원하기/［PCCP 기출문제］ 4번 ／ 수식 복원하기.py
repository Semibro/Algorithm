# 10진수로 변경하는 함수
def change_number_system_to_ten(ns, num):
    if len(num) == 1:
        return int(num)
    
    number = 0
    for index in range(len(num)):
        number += int(num[index]) * (ns ** (len(num) - 1 - index))
        
    return number

# 10진수 외의 진수로 변경하는 함수
def change_number_system_to_not_ten(ns, num):
    if num == 0:
        return "0"
    
    answer = ""
    for idx in range(2, -1, -1):
        div = num // (ns ** idx)
        
        if answer or div:
            answer += str(div)
        
        num = num % (ns ** idx)
    
    return answer

def solution(expressions):
    max_number_system = 0
    hint_expression, answer_expression = [], []
    
    # 힌트와 정답 수식을 분리, 최대 진법 찾기
    for expression in expressions:
        A, sign, B, equal, C = expression.split(" ")

        for index in range(len(A)):
            max_number_system = max(max_number_system, int(A[index]))
        for index in range(len(B)):
            max_number_system = max(max_number_system, int(B[index]))
            
        if C != "X":
            hint_expression.append(expression)
            for index in range(len(C)):
                max_number_system = max(max_number_system, int(C[index]))
        else:
            answer_expression.append(expression)        
    
    answer_number_system = []  # 계산이 가능한 진법 리스트
    
    # 진법 탐색
    for number_system in range(max_number_system+1, 10):
        flag = True  # 탐색 성공 여부 플래그
        
        for hint in hint_expression:
            A, sign, B, equal, C = hint.split(" ")
            ten_a, ten_b, ten_c = change_number_system_to_ten(number_system, A), change_number_system_to_ten(number_system, B), change_number_system_to_ten(number_system, C)
            
            if (sign == "+" and ten_a + ten_b != ten_c) or (sign == "-" and ten_a - ten_b != ten_c):
                flag = False
                break
        
        if flag:
            answer_number_system.append(number_system)
            
    answer = []        
    
    # 정답 수식 처리
    for index in range(len(answer_expression)):
        A, sign, B, equal, C = answer_expression[index].split(" ")
        answer_set = set()
        
        for ans in answer_number_system:
            ten_a, ten_b = change_number_system_to_ten(ans, A), change_number_system_to_ten(ans, B)
            if sign == "+":
                answer_set.add(change_number_system_to_not_ten(ans, ten_a + ten_b))
            else:
                answer_set.add(change_number_system_to_not_ten(ans, ten_a - ten_b))
                
        if len(answer_set) == 1:
            answer.append(f"{A} {sign} {B} = {list(answer_set)[0]}")
        else:
            answer.append(f"{A} {sign} {B} = ?")
            
    return answer