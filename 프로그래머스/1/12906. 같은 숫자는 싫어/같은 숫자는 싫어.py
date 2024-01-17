def solution(arr):
    answer = [10]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    return answer[1:]