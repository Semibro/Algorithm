def solution(sequence, k):
    # 투 포인터
    max_sum = 0
    end = 0
    interval = len(sequence)

    for start in range(len(sequence)):
        while max_sum < k and end < len(sequence):
            max_sum += sequence[end]
            end += 1
        if max_sum == k and end-1-start < interval:
            res = [start, end-1]
            interval = end-1-start
        max_sum -= sequence[start]

    return res