N = int(input())
card = dict()

for _ in range(N):
    temp = int(input())
    if temp in card:
        card[temp] += 1
    else:
        card[temp] = 1

answer = sorted(card.items(), key=lambda x: (-x[1], x[0]))
print(answer[0][0])