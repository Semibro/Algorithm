def solution(number, k):
    stack = []  # 정답 출력용 배열
    
    for item in number:
        # 스택이 비어있을 때
        if not stack:
            stack.append(item)
            continue
        
        # k 여부 판단
        if k > 0:
            while stack[-1] < item:
                stack.pop()
                k -= 1
                if not stack or k == 0:
                    break
        stack.append(item)
    
    # 정답 출력용 문자열
    answer = ""
    
    for item in stack:
        answer += item
        
    if k > 0:
        answer = answer[:-k]
        
    return answer