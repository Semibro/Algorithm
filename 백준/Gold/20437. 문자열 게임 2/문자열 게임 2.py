import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    W = input().strip()
    K = int(input())

    # defaultdict 사용하면 편하다.
    # dict를 사용하는데 어떤 형태로 사용할지 정할 수 있다.
    dictionary = defaultdict(list)
    # key: 문자, value: index list
    # ex) a: [1, 2, 3]

    # K개 이상인 문자를 딕셔너리에 저장
    for i in range(len(W)):
        if W.count(W[i]) >= K:
            dictionary[W[i]].append(i)

    # 기본적인 최소, 최대 값 설정
    min, max = 9876543210, 0

    for char, idx_list in dictionary.items():
        # 인덱스의 개수가 정확히 K개일 때
        if len(idx_list) == K:
            length = idx_list[-1] - idx_list[0] + 1
            if length < min:
                min = length
            if length > max:
                max = length
        # 인덱스의 개수가 K개보다 많을 때
        elif len(idx_list) > K:
            start_idx = 0
            while True:
                end_idx = start_idx + (K-1)
                length = idx_list[end_idx] - idx_list[start_idx] + 1
                if length < min:
                    min = length
                if length > max:
                    max = length
                if end_idx == len(idx_list)-1:
                    break
                start_idx += 1

    if min > 10000 and max == 0:
        print(-1)
    else:
        print(min, max)