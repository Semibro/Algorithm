def solution(n, info):
    max_point = -1
    answer = [-1]
    
    def dfs(index, arrows_left, ryan):
        nonlocal max_point, answer
        
        if index == 11:
            if arrows_left > 0:
                ryan[10] += arrows_left  # 남은 화살은 0점에 몰아준다. (조건에 따라 가장 작은 점수를 쏴야하기 때문에)
            
            # 라이언과 어피치 스코어 비교
            r_score, a_score = 0, 0
            for i in range(11):
                if ryan[i] == 0 and info[i] == 0:
                    continue
                if ryan[i] > info[i]:
                    r_score += 10 - i
                else:
                    a_score += 10 -i
                    
            # 라이언이 이긴 경우
            if r_score > a_score:
                point = r_score - a_score
                
                # 큰 점수차 찾기
                if point > max_point:
                    max_point = point
                    answer = ryan[:]
                # 최대 점수라면 더 작은 점수를 쏜 것으로 변경
                elif point == max_point:
                    for i in range(10, -1, -1):  # 작은 점수 비교를 위해 역으로 for문 진행
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
                        elif ryan[i] < answer[i]:
                            break
            
            if arrows_left > 0:
                ryan[10] -= arrows_left  # 재귀를 위해 되돌리기
            return
        
        # 어피치보다 화살을 1개 더 쏘는 경우
        need = info[index] + 1
        if need <= arrows_left:
            ryan[index] = need
            dfs(index+1, arrows_left-need, ryan)
            ryan[index] = 0
        
        # 화살을 안쏘는 경우
        dfs(index+1, arrows_left, ryan)
        
    dfs(0, n, [0]*11)
    
    return answer