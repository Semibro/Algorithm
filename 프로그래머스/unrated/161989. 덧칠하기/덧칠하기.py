def solution(n, m, section):
    p, ans = section[0]-1, 0
    for i in section:
        if p < i:
            p = i+m-1
            ans += 1
    return ans