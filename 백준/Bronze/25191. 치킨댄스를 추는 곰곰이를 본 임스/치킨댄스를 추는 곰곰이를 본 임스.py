N = int(input())
A, B = map(int, input().split())

if A//2 + B <= N:
    print(A//2 + B)
else:
    print(N)