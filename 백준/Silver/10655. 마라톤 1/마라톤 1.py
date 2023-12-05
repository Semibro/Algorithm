N = int(input())

# 체크포인트
CP = []
for _ in range(N):
    CP.append(list(map(int, input().split())))

distance = [0]
for i in range(N-1):
    dist = abs(CP[i][0]-CP[i+1][0]) + abs(CP[i][1]-CP[i+1][1])
    distance.append(dist)

totalDistance = sum(distance)

tempDistance = 0
minDistance = 9876543210

for i in range(1, N-1):
    tempDistance = totalDistance - (distance[i]+distance[i+1]) + abs(CP[i+1][0] - CP[i-1][0]) + abs(CP[i+1][1] - CP[i-1][1])
    minDistance = min(minDistance, tempDistance)

print(minDistance)