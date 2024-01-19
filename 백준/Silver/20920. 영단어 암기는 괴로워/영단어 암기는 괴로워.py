# N: 영어 지문에 나오는 단어의 개수  /  M: 외울 단어의 길이 기준
N, M = map(int, input().split())
check_dict = {}

for _ in range(N):
    word = input()
    if len(word) >= M:
        if word in check_dict:
            check_dict[word] += 1
        else:
            check_dict[word] = 1

sorted_dict = sorted(check_dict.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for word, count in sorted_dict:
    print(word)