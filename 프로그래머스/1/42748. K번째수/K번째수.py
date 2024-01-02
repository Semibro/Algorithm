def solution(array, commands):
    answer = []
    for i, j, k in commands:
        temp_array = sorted(array[i-1:j])
        answer.append(temp_array[k-1])
    return answer