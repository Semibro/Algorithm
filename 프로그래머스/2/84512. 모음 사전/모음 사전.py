def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    weights = [781, 156, 31, 6, 1]
    answer = 0
    
    for i in range(len(word)):
        if word[i] == "A":
            answer += 1
        else:
            answer += weights[i] * vowels.index(word[i]) + 1
        
    return answer