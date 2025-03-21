def solution(name):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    answer = 0
    
    for n in name:
        idx = alphabet.index(n)
        if idx <= 13:
            answer += idx
        else:
            answer += 26 - idx
            
    min_move = len(name) - 1  # 왼쪽으로만 이동
    for i in range(len(name)):
        next_index = i + 1
        while next_index < len(name) and name[next_index] == "A":
            next_index += 1
            
        right_left_return = i + i + (len(name) - next_index)
        left_return = (len(name) - next_index) * 2 + i
        min_move = min(min_move, right_left_return, left_return)
        
    answer += min_move
    
    return answer