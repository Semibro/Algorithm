def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        alpha = s[i]
        cnt = 0
        for j in range(i-1, -1, -1):
            cnt += 1
            if alpha == s[j]:
                answer.append(cnt)
                break
        else:
            answer.append(-1)
    return answer