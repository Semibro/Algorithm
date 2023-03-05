N, L = map(int, input().split())
sinho = []
for _ in range(N):
    D, R, G = map(int, input().split())
    sinho.append([D, R, G])  # D : 신호등 위치 / R : 빨간불 지속시간 / G : 초록불 지속시간
time = 0  # 걸린시간
dist = 0
for i in sinho:
    time += i[0]-dist
    dist += i[0] - dist
    if time % (i[1]+i[2]) >= i[1]:
        pass
    else:
        time += i[1] - (time % (i[1]+i[2]))
time += L - dist
print(time)