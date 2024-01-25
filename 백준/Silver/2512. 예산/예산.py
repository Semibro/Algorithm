N = int(input())  # 지방의 수
price = list(map(int, input().split()))  # 각 지방에 필요한 예산
M = int(input())  # 총 예산

# 총 예산보다 작으면 제일 큰 지방 예산을 출력
if sum(price) <= M:
    print(max(price))
# 총 예산으로 해결이 불가능한 경우, 이분탐색
else:
    min_value, max_value = 0, max(price)  # 이분탐색을 위한 최소, 최대값 설정

    # 이분탐색
    while min_value <= max_value:
        middle = (min_value + max_value) // 2  # 중간값(예산)
        total_price = 0  # 총 예산이 얼마가 드는지 알기 위한 변수

        # 중간값(예산)보다 크면 중간값으로 배정하고 아니면 원래 예산으로 배정
        for p in price:
            if p > middle:
                total_price += middle
            else:
                total_price += p

        # 예산보다 작으면 중간값을 최소값으로 설정해서 다시 이분탐색 아니면 최대값으로 설정해서 이분탐색
        if total_price <= M:
            min_value = middle + 1
        else:
            max_value = middle - 1

    print(max_value)