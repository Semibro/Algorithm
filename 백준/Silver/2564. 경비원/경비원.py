garo, sero = map(int, input().split())
N = int(input())
market_lst = []
for _ in range(N):
    direct, dist = map(int, input().split())
    market_lst.extend([[direct, dist]])
dong = list(map(int, input().split()))
# 1 : 북 / 2 : 남 / 3 : 서 / 4 : 동
# 남북 : 왼쪽으로부터 거리 / 동서 : 위쪽으로부터 거리

result = 0
if dong[0] == 1:  # 북
    for i in market_lst:
        if i[0] == 1:
            result += abs(dong[1] - i[1])
        elif i[0] == 2:
            if dong[1] + i[1] > (garo-dong[1]) + (garo-i[1]):
                result += (((garo-dong[1]) + (garo-i[1])) + sero)
            else:
                result += (dong[1] + i[1]) + sero
        elif i[0] == 3:
            result += (dong[1] + i[1])
        else:
            result += ((garo-dong[1]) + i[1])
elif dong[0] == 2:  # 남
    for i in market_lst:
        if i[0] == 1:
            if dong[1] + i[1] > (garo - dong[1]) + (garo - i[1]):
                result += (((garo - dong[1]) + (garo - i[1])) + sero)
            else:
                result += (dong[1] + i[1]) + sero
        elif i[0] == 2:
            result += abs(dong[1] - i[1])
        elif i[0] == 3:
            result += (dong[1] + (sero - i[1]))
        else:
            result += ((garo-dong[1]) + (sero-i[1]))
elif dong[0] == 3:  # 서
    for i in market_lst:
        if i[0] == 1:
            result += (dong[1] + i[1])
        elif i[0] == 2:
            result += ((sero-dong[1]) + i[1])
        elif i[0] == 3:
            result += abs(dong[1] - i[1])
        else:
            if dong[1] + i[1] > (sero - dong[1]) + (sero - i[1]):
                result += (((sero - dong[1]) + (sero - i[1])) + garo)
            else:
                result += (dong[1] + i[1]) + garo
else:  # 동
    for i in market_lst:
        if i[0] == 1:
            result += (dong[1] + (garo - i[1]))
        elif i[0] == 2:
            result += ((sero - dong[1]) + (garo - i[1]))
        elif i[0] == 3:
            if dong[1] + i[1] > (sero - dong[1]) + (sero - i[1]):
                result += (((sero - dong[1]) + (sero - i[1])) + garo)
            else:
                result += (dong[1] + i[1]) + garo
        else:
            result += abs(dong[1] - i[1])

print(result)