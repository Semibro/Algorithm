import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
if M == 0:
    print(min(len(str(N)), abs(100-N)))
else:
    miss_btn = list(map(int, input().split()))
    res = abs(100-N)
    for i in range(1000001):
        for j in str(i):
            if int(j) in miss_btn:
                break
        else:
            res = min(res, abs(N-i)+len(str(i)))
    print(res)