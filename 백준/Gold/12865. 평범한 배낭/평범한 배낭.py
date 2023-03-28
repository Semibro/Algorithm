N, K = map(int, input().split())
W, V = [], []
bag = [0] * (K+1)
for _ in range(N):
    weight, value = map(int, input().split())
    W.append(weight)
    V.append(value)
for i in range(N):
    for j in range(K, 0, -1):
        if W[i] <= j:
            bag[j] = max(bag[j], bag[j-W[i]]+V[i])
print(bag[-1])