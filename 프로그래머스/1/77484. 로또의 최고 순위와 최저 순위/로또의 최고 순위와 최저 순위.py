def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    win_set = set(win_nums)  # O(1)로 접근하기 위해 set으로 변경
    
    zero_count = lottos.count(0)
    match_count = 0
    
    for lotto in lottos:
        if lotto in win_set:
            match_count += 1
            
    max_rank = rank[match_count + zero_count]
    min_rank = rank[match_count]
    
    return [max_rank, min_rank]
