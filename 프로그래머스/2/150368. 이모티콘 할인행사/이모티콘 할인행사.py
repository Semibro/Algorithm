from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]  # 가능한 할인율
    max_plus_users = 0
    max_sales = 0

    # 가능한 모든 할인율 조합을 탐색
    for discounts in product(discount_rates, repeat=len(emoticons)):
        plus_users = 0
        total_sales = 0
        
        for discount_rate, min_price in users:
            total_cost = 0
            # 할인율에 맞춰 각 사용자가 구매할 이모티콘 계산
            for i in range(len(emoticons)):
                if discounts[i] >= discount_rate:
                    total_cost += emoticons[i] * (1 - discounts[i] / 100)
            
            # 구매 비용이 일정 가격 이상이면 플러스 서비스 가입
            if total_cost >= min_price:
                plus_users += 1
            else:
                total_sales += total_cost
        
        # 가입자 수가 더 많으면 무조건 업데이트, 같을 경우 판매액 비교
        if plus_users > max_plus_users or (plus_users == max_plus_users and total_sales > max_sales):
            max_plus_users = plus_users
            max_sales = total_sales

    return [max_plus_users, int(max_sales)]