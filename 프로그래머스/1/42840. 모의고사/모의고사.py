def solution(answers):
    result = [0, 0, 0] # 맞춘 문제를 체크하기 위한 리스트
    
    # 수포자
    noMath1 = [1, 2, 3, 4, 5]
    noMath2 = [2, 1, 2, 3, 2, 4, 2, 5]
    noMath3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 맞춘 문제 확인
    for i in range(len(answers)):
        ans = answers[i]
        if noMath1[i%len(noMath1)] == ans:
            result[0] += 1
        if noMath2[i%len(noMath2)] == ans:
            result[1] += 1
        if noMath3[i%len(noMath3)] == ans:
            result[2] += 1
            
    # 결과 출력
    answer = []
    for i in range(len(result)):
        if result[i] == max(result):
            answer.append(i+1)
    return answer