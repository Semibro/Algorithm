import sys
from collections import defaultdict

input = sys.stdin.readline

# N: 접시 수, d: 초밥의 가짓수, k: 연속해서 먹는 접시의 수, c: 쿠폰 번호
N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
sushi += sushi[:k - 1]

eat_sushi = defaultdict(int)
answer = 0

for i in range(k):
    eat_sushi[sushi[i]] += 1
    
if c in eat_sushi:
    answer = len(eat_sushi)
else:
    answer = len(eat_sushi) + 1
    
for i in range(1, N):
    out_sushi = sushi[i - 1]
    in_sushi = sushi[i + k - 1]
    
    eat_sushi[out_sushi] -= 1
    eat_sushi[in_sushi] += 1
    
    if eat_sushi[out_sushi] == 0:
        del eat_sushi[out_sushi]
        
    if c in eat_sushi:
        answer = max(answer, len(eat_sushi))
    else:
        answer = max(answer, len(eat_sushi) + 1)

print(answer)