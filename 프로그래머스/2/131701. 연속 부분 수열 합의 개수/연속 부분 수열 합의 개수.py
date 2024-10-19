def solution(elements):
    n = len(elements)
    elements_extended = elements * 2
    
    sums_set = set()
    
    for length in range(1, n+1):
        for start in range(n):
            subarray_sum = sum(elements_extended[start:start+length])
            sums_set.add(subarray_sum)
    
    return len(sums_set)