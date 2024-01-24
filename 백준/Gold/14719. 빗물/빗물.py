H, W = map(int, input().split())  # 세로 H, 가로 W
block = list(map(int, input().split()))

answer = 0
for i in range(1, W-1):
    left = max(block[:i])
    right = max(block[i+1:])
    min_value = min(left, right)

    if block[i] < min_value:
        answer += min_value - block[i]

print(answer)