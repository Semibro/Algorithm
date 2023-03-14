import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    lst_1 = set(map(int, input().split()))
    M = int(input())
    lst_2 = list(map(int, input().split()))

    for i in lst_2:
        if i in lst_1:
            print(1)
        else:
            print(0)