N = int(input())  # 굴다리의 길이
M = int(input())  # 가로등의 개수
x = list(map(int, input().split()))  # 가로등의 위치

# 가로등 사이의 거리 중 제일 긴 거리 구하기
max_value = 0
for i in range(M-1):
    max_value = max(max_value, x[i+1]-x[i])

# 사이거리, 0부터 첫번째 가로등, 마지막 가로등부터 끝 중 제일 긴 값 구하기
print(max((max_value+1)//2, x[0], N-x[-1]))