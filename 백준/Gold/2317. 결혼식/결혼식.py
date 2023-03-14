N, K = map(int, input().split())
lion, people = [], []
res = 0
for _ in range(K):
    lion.append(int(input()))
for _ in range(N-K):
    people.append(int(input()))
for i in range(K-1):
    res += abs(lion[i] - lion[i+1])
if len(people) == 0:
    print(res)
else:
    max_v = max(people)
    min_v = min(people)
    if max(lion) < max_v:
        res += min(abs(lion[0]-max_v), abs(lion[-1]-max_v), 2*abs(max(lion)-max_v))
    if min(lion) > min_v:
        res += min(abs(lion[0]-min_v), abs(lion[-1]-min_v), 2*abs(min(lion)-min_v))
    print(res)