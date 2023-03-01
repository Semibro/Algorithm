garo, sero = map(int, input().split())
N = int(input())
w = [0, garo]
h = [0, sero]
for _ in range(N):
    c, t = map(int, input().split())
    if c == 0:
        h.append(t)
    else:
        w.append(t)

w.sort()
h.sort()

result_w = []
result_h = []

for i in range(len(w)-1):
    result_w.append(w[i+1]-w[i])
for i in range(len(h)-1):
    result_h.append(h[i+1]-h[i])
print(f'{max(result_h) * max(result_w)}')