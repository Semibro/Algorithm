def solution(n, left, right):
    """
    [ 문제 해결 아이디어 ]
    배열에서 (i, j)에 위치한 값은 max(i, j) + 1이다.
    """
    
    answer = []
    
    for i in range(left, right+1):
        row = i // n
        col = i % n
        answer.append(max(row, col) + 1)
        
    return answer