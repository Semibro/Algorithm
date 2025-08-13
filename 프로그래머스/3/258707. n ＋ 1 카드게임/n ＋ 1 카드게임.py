def solution(coin, cards):
    N = len(cards)
    target = N + 1
    my_cards = set(cards[:N//3])
    open_cards = set()
    
    idx = N // 3
    round_count = 1
    
    while idx < N:
        # 라운드가 시작하면 카드 2장 뽑기
        open_cards.add(cards[idx])
        open_cards.add(cards[idx + 1])
        idx += 2
        
        # 라운드가 끝났는지 알기 위한 플래그
        flag = False
        
        # 페어를 찾았는지 확인할 플래그
        found_pair = False
        # 페어를 찾으면 저장할 변수
        card_one, card_two = -1, -1
        
        for card in my_cards:
            if (target - card) in my_cards:
                card_one, card_two = card, target - card
                found_pair = True
                break
                
        if found_pair:
            my_cards.remove(card_one)
            my_cards.remove(card_two)
            flag = True
            
        if not flag and coin >= 1:
            for card in my_cards:
                if (target - card) in open_cards:
                    card_one, card_two = card, target - card
                    found_pair = True
                    break
            
            if found_pair:
                coin -= 1
                my_cards.remove(card_one)
                open_cards.remove(card_two)
                flag = True
                
        if not flag and coin >= 2:
            for card in open_cards:
                if (target - card) in open_cards:
                    card_one, card_two = card, target - card
                    found_pair = True
                    break

            if found_pair:
                coin -= 2
                open_cards.remove(card_one)
                open_cards.remove(card_two)
                flag = True
                    
        if flag:
            round_count += 1
        else:
            break
            
    return round_count