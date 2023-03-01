K = int(input())
ground = []

for _ in range(6):
    direct, length = map(int, input().split())
    ground.append([direct, length])

max_w = max_h = 0
max_idx_w = max_idx_h = 0

for i in range(6):
    if ground[i][0] == 1 or ground[i][0] == 2:
        if ground[i][1] > max_w:
            max_w = ground[i][1]
            max_idx_w = i
    else:
        if ground[i][1] > max_h:
            max_h = ground[i][1]
            max_idx_h = i

full_size = max_w * max_h
cut_size = abs(ground[(max_idx_w-1)%6][1] - ground[(max_idx_w+1)%6][1]) * abs(ground[(max_idx_h-1)%6][1] - ground[(max_idx_h+1)%6][1])

print(K * (full_size-cut_size))