def solution(coin, cards):
    # 전체 카드의 개수
    n = len(cards)
    # 페어를 만들기 위한 목표 합계 (문제 조건에 따라 항상 n + 1)
    target = n + 1
    
    # 처음 n/3 개의 카드는 비용 없이 가집니다. (set으로 만들어 O(1) 시간 복잡도로 탐색 가능)
    my_cards = set(cards[:n//3])
    # 라운드를 진행하며 새로 뽑지만, 아직 구매하지 않은 카드들.
    pending_cards = set()
    
    # 현재 라운드 번호, 1라운드부터 시작
    round_count = 1
    # 다음에 뽑을 카드의 인덱스
    card_idx = n // 3
    
    # 게임 라운드 진행 루프. 뽑을 카드가 남아있는 동안 계속됩니다.
    while card_idx < n:
        # 매 라운드 시작 시, 카드 덱에서 2장의 카드를 뽑아 'pending_cards'에 추가합니다.
        pending_cards.add(cards[card_idx])
        pending_cards.add(cards[card_idx+1])
        card_idx += 2
        
        # 다음 라운드로 진행하기 위해 페어를 만들어야 합니다.
        # 가장 비용이 적게 드는 방법(0코인 -> 1코인 -> 2코인)부터 순서대로 확인합니다.
        
        # --- 방법 1: 비용 0 (초기 카드 2장 사용) ---
        found_pair = False
        # 내 카드 중에서 합이 target이 되는 페어가 있는지 탐색합니다.
        for card in my_cards:
            if (target - card) in my_cards:
                # 페어를 찾았으므로, 사용한 카드들을 제거합니다.
                my_cards.remove(card)
                my_cards.remove(target - card)
                found_pair = True
                break # 페어를 찾았으므로 더 이상 탐색할 필요가 없습니다.
        
        if found_pair:
            round_count += 1 # 다음 라운드로 진출
            continue         # 현재 라운드를 통과했으므로 다음 루프를 시작합니다.

        # --- 방법 2: 비용 1 (초기 카드 1장 + 새로 뽑은 카드 1장) ---
        # 코인이 1개 이상 있을 때만 시도할 수 있습니다.
        if coin >= 1:
            found_pair = False
            # 내 카드와 새로 뽑은 카드(pending)로 페어가 되는 조합을 탐색합니다.
            for card in my_cards:
                if (target - card) in pending_cards:
                    # 페어를 찾았으므로 코인 1개를 소모하고, 각 덱에서 카드를 제거합니다.
                    coin -= 1
                    my_cards.remove(card)
                    pending_cards.remove(target - card)
                    found_pair = True
                    break
            
            if found_pair:
                round_count += 1 # 다음 라운드로 진출
                continue         # 현재 라운드를 통과했으므로 다음 루프를 시작합니다.

        # --- 방법 3: 비용 2 (새로 뽑은 카드 2장) ---
        # 코인이 2개 이상 있을 때만 시도할 수 있습니다.
        if coin >= 2:
            found_pair = False
            # 새로 뽑은 카드(pending) 중에서 페어가 되는 조합을 탐색합니다.
            for card in pending_cards:
                if (target - card) in pending_cards:
                    # 페어를 찾았으므로 코인 2개를 소모하고, 덱에서 카드를 제거합니다.
                    coin -= 2
                    pending_cards.remove(card)
                    pending_cards.remove(target - card)
                    found_pair = True
                    break
            
            if found_pair:
                round_count += 1 # 다음 라운드로 진출
                continue         # 현재 라운드를 통과했으므로 다음 루프를 시작합니다.

        # 위 3가지 방법으로 페어를 만들 수 없다면 더 이상 라운드를 진행할 수 없습니다.
        # continue가 실행되지 않았다면 루프는 여기서 종료됩니다.
        break
            
    return round_count