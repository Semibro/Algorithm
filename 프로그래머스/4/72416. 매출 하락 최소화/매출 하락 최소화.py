# Dynamic Programming on Trees

import sys
sys.setrecursionlimit(300000)

def solution(sales, links):
    N = len(sales)
    
    # 트리 구조 만들기 (부모 -> 자식)
    tree = [[] for _ in range(N + 1)]
    for parent, child in links:
        tree[parent].append(child)
        
    # DP 테이블 생성
    dp = [[0, 0] for _ in range(N + 1)]
    
    # DFS 함수
    def dfs(u):        
        # 리프 노드인 경우
        if not tree[u]:
            dp[u][0] = 0  # node가 참석하지 않으면 비용 0
            dp[u][1] = sales[u-1]  # node가 참석하면 자신의 매출액이 비용
            return
        
        # 후위순회 (자식 -> 부모로 dp계산)
        for v in tree[u]:
            dfs(v)
            
        # --- dp[u][1] 계산 (u가 참석하는 경우) ---
        # 본인이 참석하므로 자신의 매출액을 비용에 더한다
        # 팀 중에 한 명이 참석해서 조건을 만족했으므로, 자식 중에는 참석/불참 중 최소 비용을 선택
        cost_u_attends = sales[u-1]
        for v in tree[u]:
            cost_u_attends += min(dp[v][0], dp[v][1])
        dp[u][1] = cost_u_attends
        
        # --- dp[u][0] 계산 (u가 불참하는 경우) ---
        # u가 참석하지 않으므로, 자식 중에 한 명은 반드시 참석해야 한다
        cost_u_not_attends = 0
        min_cost = 9876543210  # 참석시켜야 할 때의 최소 비용
        is_condition = False  # 조건이 만족됐는지 체크할 변수
        
        for v in tree[u]:
            # 자식의 참석/불참 중 최솟값 가져오기
            cost_u_not_attends += min(dp[v][0], dp[v][1])
            
            # 만약 참석하는 것이 더 저렴하다면 팀 조건은 만족
            if dp[v][1] < dp[v][0]:
                is_condition = True
            
            # 만약 불참하는 것이 더 저렴한 경우
            # 이 자식을 강제로 참석시켰을 때, 비용을 계산
            min_cost = min(min_cost, dp[v][1] - dp[v][0])
            
        # 만약 모든 자식이 불참하는 경우 강제 참석시켰을 때, 비용이 가장 저렴한 자식을 참석
        if not is_condition:
            cost_u_not_attends += min_cost
            
        dp[u][0] = cost_u_not_attends
        
    # dfs로 탐색
    dfs(1)
        
    return min(dp[1][0], dp[1][1])