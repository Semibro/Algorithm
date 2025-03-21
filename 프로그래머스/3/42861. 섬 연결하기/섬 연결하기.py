def solution(n, costs):
    # Kruskal Algorithm
    # 1. 간선을 비용 순서대로 정렬
    costs.sort(key = lambda x: x[2])
    
    # 2. 각 노드의 부모를 자기 자신으로 초기화
    parent = [i for i in range(n)]
    
    # 3. union-find를 위한 find 함수 생성
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    # 4. union-find를 위한 union 함수 생성
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        
        return False
    
    total_cost = 0
    edge_count = 0
    
    # 5. 간선을 하나씩 선택하면서 Minimum Spanning Tree(최소 신장 트리) 구성
    for a, b, c in costs:
        if union(a, b):
            total_cost += c
            edge_count += 1
            if edge_count == n - 1:
                break
                
    return total_cost