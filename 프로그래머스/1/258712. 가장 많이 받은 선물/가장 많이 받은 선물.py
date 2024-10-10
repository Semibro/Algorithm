def solution(friends, gifts):
    giftCount = {}  # 선물을 주고 받은 횟수
    giftPoint = {}  # 선물 지수
    
    # 배열 기본 상태 설정
    for friend in friends:
        giftCount[friend] = {}
        giftPoint[friend] = 0
        
    for gift in gifts:
        A, B = gift.split(" ")  # A와 B를 구분
        
        # 선물 주고 받은 횟수 처리
        if B in giftCount[A]:
            giftCount[A][B] += 1
        else:
            giftCount[A][B] = 1
            
        # 선물 지수 처리
        giftPoint[A] += 1
        giftPoint[B] -= 1
        
    answer = [0 for _ in friends]  # 다음 달에 받을 선물의 개수를 저장하는 리스트
    
    for i in range(len(friends)):
        one = friends[i]  # 친구1
        
        for j in range(i+1, len(friends)):
            two = friends[j]  # 친구2
            
            # 친구1 -> 친구2
            if two in giftCount[one]:
                one_to_two = giftCount[one][two]  # 친구1이 친구2에게 선물을 줬을 경우
            else:
                one_to_two = 0  # 선물을 주지 않았을 경우
                
            # 친구2 -> 친구1
            if one in giftCount[two]:
                two_to_one = giftCount[two][one]
            else:
                two_to_one = 0
                
            # 선물 로직 적용
            if one_to_two > two_to_one:
                answer[i] += 1
            elif two_to_one > one_to_two:
                answer[j] += 1
            elif one_to_two == two_to_one:  # 선물을 준 횟수가 같다면 "선물 지수" 비교
                one_giftPoint, two_giftPoint = giftPoint[one], giftPoint[two]  # 선물 지수
                
                if one_giftPoint > two_giftPoint:
                    answer[i] += 1
                elif two_giftPoint > one_giftPoint:
                    answer[j] += 1
    
    # 정답 출력
    return max(answer)