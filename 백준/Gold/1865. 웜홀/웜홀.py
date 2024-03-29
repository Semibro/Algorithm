import sys
input = sys.stdin.readline

# 벨만-포드 알고리즘
# 벨만-포드 알고리즘은 간선의 가중치가 음수가 있을 때 사용
# 다익스트라 알고리즘의 경우 간선의 가중치가 전부 양수일 때만 사용
# 이 문제의 경우 음수순환의 여부를 묻는 문제이므로 dist[s] != 9876543210 을 할 필요가 없다.
def bellman_ford(start):
    dist = [9876543210] * (N+1)  # 거리 측정을 위한 dist 리스트 생성
    dist[start] = 0  # 시작위치를 0으로 설정
    for i in range(N):  # N만큼 확인
        for s, e, t in road_wormhole:  # 간선을 꺼내서 더 적은 방향이 있는지 확인
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == N-1:  # 혹시라도 마지막에서 갱신이 일어난다면, 음수순환이 존재하는 것이므로 True를 반환
                    return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    road_wormhole = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        # 도로의 경우 방향이 없다고 문제에서 주어줬으므로 무방향 그래프로 작성
        road_wormhole.append((S, E, T))
        road_wormhole.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        road_wormhole.append((S, E, -T))  # 웜홀의 경우 시간이 감소한다고 했으므로 음수로 처리

    result = bellman_ford(1)  # 1번부터 N-1번까지 검사할 것이므로 시작값이 1을 넣어준다.

    if result:  # 결과가 양수가 나온다면 음수순환이 존재한다는 것이므로 YES반환
        print('YES')
    else:  # 아니라면 NO 반환
        print('NO')