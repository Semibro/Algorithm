# 문제에서 "~의 최댓값을 최소화" 또는 "~최솟값을 최대화"와 같은 문구가 등장한다면 "파라메트릭서치"를 생각해봐야한다.

import sys
sys.setrecursionlimit(10**5)

def solution(k, num, links):
    N = len(num)
    
    # 루트 노드 찾기
    visited = [False] * N
    for left, right in links:
        if left != -1:
            visited[left] = True
        if right != -1:
            visited[right] = True
            
    root_node = -1
    for idx in range(N):
        if not visited[idx]:
            root_node = idx
            break
            
    # 파라메트릭 서치
    left, right = max(num), sum(num)
    answer = 0
    group_count = 0
    
    def dfs(node, limit):
        nonlocal group_count
        
        if node == -1:
            return 0
        
        left_sum = dfs(links[node][0], limit)
        right_sum = dfs(links[node][1], limit)
        
        current = num[node]
        
        if current + left_sum + right_sum <= limit:
            return current + left_sum + right_sum
        
        if current + min(left_sum, right_sum) <= limit:
            group_count += 1
            return current + min(left_sum, right_sum)
        
        group_count += 2
        return current
    
    while left <= right:
        mid = (left + right) // 2
        
        group_count = 0
        dfs(root_node, mid)
        
        total_group_count = group_count + 1
        
        if total_group_count <= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer