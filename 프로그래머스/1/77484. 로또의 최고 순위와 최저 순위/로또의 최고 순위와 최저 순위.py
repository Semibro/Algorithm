def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    win_nums_match_count = 0
    
    for lotto in lottos:
        if lotto != 0 and lotto in win_nums:
            win_nums_match_count += 1
            
    def check_lotto(num):
        if num == 6:
            return 1
        elif num == 5:
            return 2
        elif num == 4:
            return 3
        elif num == 3:
            return 4
        elif num == 2:
            return 5
        else:
            return 6
        
    answer = [check_lotto(zero_count + win_nums_match_count), check_lotto(win_nums_match_count)]
    
    return answer