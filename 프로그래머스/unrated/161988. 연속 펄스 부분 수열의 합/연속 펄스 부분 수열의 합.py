def solution(sequence):
    dp = [0]
    for i in range(len(sequence)):
        if i % 2 == 0:
            dp.append(dp[-1] + sequence[i])
        else:
            dp.append(dp[-1] - sequence[i])
    answer = abs(max(dp) - min(dp))
    return answer