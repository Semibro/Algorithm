def solution(survey, choices):
    answer = ''
    mbti = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for idx in range(len(survey)):
        if choices[idx] < 4:
            mbti[survey[idx][0]] += abs(choices[idx]-4)
        elif choices[idx] > 4:
            mbti[survey[idx][1]] += abs(choices[idx]-4)
        else:
            pass
    
    # R T
    if mbti['R'] >= mbti['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    # C F
    if mbti['C'] >= mbti['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    # J M
    if mbti['J'] >= mbti['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    # A N
    if mbti['A'] >= mbti['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer