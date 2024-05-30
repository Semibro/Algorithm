T = int(input())

for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    answer, max_price = 0, days[-1]

    for i in range(N-2, -1, -1):
        if days[i] > max_price:
            max_price = days[i]
        elif days[i] < max_price:
            answer += max_price - days[i]

    print(answer)