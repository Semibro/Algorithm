N = int(input())
tanghuru = list(map(int, input().split()))
start, answer, length, fruits = 0, 0, 0, dict()

for i in range(N):
    # 탕후루 하나씩 확인
    if tanghuru[i] in fruits:
        fruits[tanghuru[i]] += 1
    else:
        fruits[tanghuru[i]] = 1

    # 길이 확인
    if len(fruits) > 2:
        while len(fruits) > 2:
            fruits[tanghuru[start]] -= 1
            if fruits[tanghuru[start]] == 0:
                fruits.pop(tanghuru[start])
            start += 1
    
    answer = max(answer, sum(fruits.values()))

print(answer)