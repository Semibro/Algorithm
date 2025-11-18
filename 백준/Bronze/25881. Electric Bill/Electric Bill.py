import sys

input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())

for _ in range(n):
    v = int(input())

    if v <= 1000:
        print(v, v * a)
    else:
        temp_v = v - 1000
        print(v, 1000 * a + temp_v * b)