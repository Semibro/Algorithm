from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    dice_idx = list(range(n))
    best_win = -1
    best_choice = None

    for comb in combinations(dice_idx, n//2):
        A_dice = list(comb)
        B_dice = [i for i in dice_idx if i not in A_dice]

        A_sums = [sum(vals) for vals in product(*[dice[i] for i in A_dice])]
        B_sums = [sum(vals) for vals in product(*[dice[i] for i in B_dice])]

        B_sums.sort()

        win_count = 0
        for a_sum in A_sums:
            win_count += bisect_left(B_sums, a_sum)

        if win_count > best_win:
            best_win = win_count
            best_choice = A_dice

    return [x + 1 for x in sorted(best_choice)]