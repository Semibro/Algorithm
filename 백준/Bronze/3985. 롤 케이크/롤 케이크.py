L = int(input())  # 롤케이크 길이
N = int(input())  # 방청객 숫자
people = []
rollcake = [0] * (L+1)
for _ in range(N):
    P, K = map(int, input().split())
    people.append([P, K])
max_v = 0
max_idx = 0
for i in range(1, N+1):
    if abs(people[i-1][0] - people[i-1][1]) > max_v:
        max_v = abs(people[i-1][0] - people[i-1][1])
        max_idx = i

for i in range(1, N+1):
    for j in range(people[i-1][0], people[i-1][1]+1):
        if rollcake[j] == 0:
            rollcake[j] = i

result = 0
result_idx = 0
for i in range(1, N+1):
    res = rollcake.count(i)
    if res > result:
        result = res
        result_idx = i

print(max_idx)
print(result_idx)