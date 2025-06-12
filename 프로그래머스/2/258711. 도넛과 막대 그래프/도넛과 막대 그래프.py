# [ 문제 설명 ]
# 도넛 모양 그래프 : 크기가 n인 도넛 모양은 n개의 정점과 n개의 간선으로 구성
# 막대 모양 그래프 : 크기가 n인 막대 모양은 n개의 정점과 n-1개의 간선으로 구성
# 8자 모양 그래프 : 크기가 n인 8자 모양은 2n+1개의 정점과 2n+2개의 간선으로 구성
# edges = [a, b]  a -> b 간선
# result = [생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수]

# [문제 풀이 핵심]
# 각 정점에서 들어오고 나간 간선의 개수로 해당 정점이 무엇인지를 파악한다.
# '생성된 정점'은 나가는 간선의 수가 2 이상, 들어오는 간선의 수가 0
# '막대 모양 그래프'의 수는 나가는 간선의 수가 0, 들어오는 간선의 수가 1
# '8자 모양 그래프'의 수는 나가는 간선의 수가 2, 들어오는 간선의 수도 2
# '도넛 모양 그래프'는 '생성된 정점'의 나가는 간선의 수에서 막대 모양 그래프와 8자 모양 그래프의 개수를 빼서 구한다.
# 생성된 정점에서 들어오는 간선이 있을 수 있으므로 해당 경우를 처리해야함.


def solution(edges):
    answer = [0, 0, 0, 0]
    
    # 들어오고 나간 간선을 저장할 dictionary
    in_out_edge = {}
    for a, b in edges:
        if a not in in_out_edge:
            in_out_edge[a] = [0, 0]  # a = [in edges, out edges]
        in_out_edge[a][1] += 1
        
        if b not in in_out_edge:
            in_out_edge[b] = [0, 0]
        in_out_edge[b][0] += 1
        
    # 생성된 정점, 막대 모양, 8자 모양 찾기
    for key in in_out_edge.keys():
        if in_out_edge[key][0] == 0 and in_out_edge[key][1] >= 2:
            answer[0] = key
        elif in_out_edge[key][0] > 0 and in_out_edge[key][1] == 0:
            answer[2] += 1
        elif in_out_edge[key][0] >= 2 and in_out_edge[key][1] >= 2:
            answer[3] += 1
            
    # 도넛 모양 찾기
    answer[1] = in_out_edge[answer[0]][1] - answer[2] - answer[3]
            
    return answer