def solution(cards):
    N = len(cards)
    visited = [0 for _ in range(N)]
    
    # 상자 열기
    for i in range(1, N+1):
        index = i - 1
        
        if visited[index] != 0:
            continue
            
        while True:
            visited[index] = i
            index = cards[index] - 1
            
            if visited[index] != 0:
                break
        
    count_list = [0 for _ in range(N + 1)]
    for num in range(1, N+1):
        count_list[num] = visited.count(num)
        
    # 2개의 최대값 구하기
    one, two = 0, 0
    for i in range(1, N+1):
        if one < count_list[i]:
            temp_one = one
            one = count_list[i]
            two = temp_one
        else:
            if two < count_list[i]:
                two = count_list[i]
                
    return one * two