N = int(input())
dice = []
for _ in range(N):
    a = list(map(int, input().split()))
    dice.append(a)
    # [[2, 3, 1, 6, 5, 4], [3, 1, 2, 4, 6, 5], [5, 6, 4, 1, 3, 2], [1, 3, 6, 2, 4, 5], [4, 1, 6, 5, 2, 3]]
# A(0)-F(5) / B(1)-D(3) / C(2)-E(4)
result = []
for i in dice[0]:
    sum_list = []
    idx = 0
    while idx != N:
        if i == 1:
            if dice[idx].index(i) == 0:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][5]
                idx += 1
            elif dice[idx].index(i) == 1:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][3]
                idx += 1
            elif dice[idx].index(i) == 2:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][4]
                idx += 1
            elif dice[idx].index(i) == 3:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][1]
                idx += 1
            elif dice[idx].index(i) == 4:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][2]
                idx += 1
            elif dice[idx].index(i) == 5:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][0]
                idx += 1
        elif i == 2:
            if dice[idx].index(i) == 0:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][5]
                idx += 1
            elif dice[idx].index(i) == 1:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][3]
                idx += 1
            elif dice[idx].index(i) == 2:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][4]
                idx += 1
            elif dice[idx].index(i) == 3:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][1]
                idx += 1
            elif dice[idx].index(i) == 4:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][2]
                idx += 1
            elif dice[idx].index(i) == 5:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][0]
                idx += 1
        elif i == 3:
            if dice[idx].index(i) == 0:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][5]
                idx += 1
            elif dice[idx].index(i) == 1:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][3]
                idx += 1
            elif dice[idx].index(i) == 2:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][4]
                idx += 1
            elif dice[idx].index(i) == 3:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][1]
                idx += 1
            elif dice[idx].index(i) == 4:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][2]
                idx += 1
            elif dice[idx].index(i) == 5:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][0]
                idx += 1
        elif i == 4:
            if dice[idx].index(i) == 0:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][5]
                idx += 1
            elif dice[idx].index(i) == 1:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][3]
                idx += 1
            elif dice[idx].index(i) == 2:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][4]
                idx += 1
            elif dice[idx].index(i) == 3:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][1]
                idx += 1
            elif dice[idx].index(i) == 4:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][2]
                idx += 1
            elif dice[idx].index(i) == 5:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][0]
                idx += 1
        elif i == 5:
            if dice[idx].index(i) == 0:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][5]
                idx += 1
            elif dice[idx].index(i) == 1:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][3]
                idx += 1
            elif dice[idx].index(i) == 2:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][4]
                idx += 1
            elif dice[idx].index(i) == 3:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][1]
                idx += 1
            elif dice[idx].index(i) == 4:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][2]
                idx += 1
            elif dice[idx].index(i) == 5:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][0]
                idx += 1
        elif i == 6:
            if dice[idx].index(i) == 0:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][5]
                idx += 1
            elif dice[idx].index(i) == 1:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][3]
                idx += 1
            elif dice[idx].index(i) == 2:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][4]
                idx += 1
            elif dice[idx].index(i) == 3:
                sum_list.append(max(dice[idx][0], dice[idx][2], dice[idx][4], dice[idx][5]))
                i = dice[idx][1]
                idx += 1
            elif dice[idx].index(i) == 4:
                sum_list.append(max(dice[idx][0], dice[idx][1], dice[idx][3], dice[idx][5]))
                i = dice[idx][2]
                idx += 1
            elif dice[idx].index(i) == 5:
                sum_list.append(max(dice[idx][1], dice[idx][2], dice[idx][3], dice[idx][4]))
                i = dice[idx][0]
                idx += 1
    result.append(sum(sum_list))

print(max(result))