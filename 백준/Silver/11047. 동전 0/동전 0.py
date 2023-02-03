n, k = map(int, input().split())
coin_lst = []
cnt = 0
for _ in range(n):
    coin = int(input())
    coin_lst.append(coin)

for i in range(len(coin_lst)-1, -1, -1):
    if k - coin_lst[i] >= 0:
        cnt += k//coin_lst[i]
        k = k - coin_lst[i] * (k//coin_lst[i])
        if k == 0:
            break

print(cnt)