N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]

for idx in range(1, N):
    RGB[idx][0] += min(RGB[idx-1][1], RGB[idx-1][2])
    RGB[idx][1] += min(RGB[idx-1][0], RGB[idx-1][2])
    RGB[idx][2] += min(RGB[idx-1][0], RGB[idx-1][1])

print(min(RGB[-1]))