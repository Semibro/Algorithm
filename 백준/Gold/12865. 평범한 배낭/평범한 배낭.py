N, K = map(int, input().split())
bag = [0] * (K+1)
for _ in range(N):
    weight, value = map(int, input().split())
    for j in range(K, 0, -1):
        if weight <= j:
            bag[j] = max(bag[j], bag[j-weight]+value)
print(bag[-1])