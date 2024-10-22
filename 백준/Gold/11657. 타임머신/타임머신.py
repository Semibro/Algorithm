############
# Solution #
############

N, M = map(int, input().split())
graph = []
INF = 9876543210
distance = [INF for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

def bellman_ford(start):
    distance[start] = 0

    for i in range(N):
        for j in range(M):
            currNode = graph[j][0]
            nextNode = graph[j][1]
            cost = graph[j][2]

            if distance[currNode] != INF and distance[nextNode] > distance[currNode] + cost:
                distance[nextNode] = distance[currNode] + cost
                if i == N-1:
                    return True

    return False

checkNegativeCycle = bellman_ford(1)

if checkNegativeCycle:
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])