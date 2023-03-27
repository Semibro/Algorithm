import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    mbti = list(input().split())
    result = 100000
    if N > 32:
        print(0)
    else:
        for i in range(0, N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    bin_V = 0
                    for d in range(4):
                        if mbti[i][d] != mbti[j][d]:
                            bin_V += 1
                        if mbti[i][d] != mbti[k][d]:
                            bin_V += 1
                        if mbti[j][d] != mbti[k][d]:
                            bin_V += 1
                    if result > bin_V:
                        result = bin_V
        print(result)