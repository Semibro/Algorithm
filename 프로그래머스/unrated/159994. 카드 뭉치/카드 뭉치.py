def solution(cards1, cards2, goal):
    answer = "Yes"
    idx1, idx2 = 0, 0
    for i in goal:
        if len(cards1) > idx1 and cards1[idx1] == i:
            idx1 += 1
        elif len(cards2) > idx2 and cards2[idx2] == i:
            idx2 += 1
        else:
            answer = "No"
            break
    return answer