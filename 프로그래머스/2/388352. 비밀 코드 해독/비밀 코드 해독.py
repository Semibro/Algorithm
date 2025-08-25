from itertools import combinations

def solution(n, q, ans):
    l = len(q[0])
    m = len(ans)
    temp = [idx for idx in range(1, n+1)]
    comb = [combination for combination in combinations(temp, l)]
    answer = 0
    
    for c in comb:
        res = 0
        
        for idx in range(m):
            count = 0
            
            for item in c:
                if item in q[idx]:
                    count += 1
                    
            if ans[idx] == count:
                res += 1
                
        if res == m:
            answer += 1
            
    return answer