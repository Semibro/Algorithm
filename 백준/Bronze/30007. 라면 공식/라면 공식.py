# W : 필요한 물의 양
# A : 라면 계수
# B : 기본 물의 양
# X : 끓일 라면 수
# W = A(X-1) + B

N = int(input())
for i in range(N):
    A, B, X = map(int, input().split())
    print(A * (X-1)+B)