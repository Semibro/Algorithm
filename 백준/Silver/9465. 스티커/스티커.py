T = int(input())
for _ in range(T):
    n = int(input())
    line_1 = list(map(int, input().split()))
    line_2 = list(map(int, input().split()))

    if n > 1:
        line_1[1] += line_2[0]
        line_2[1] += line_1[0]

    for idx in range(2, n):
        line_1[idx] += max(line_2[idx-1], line_2[idx-2])
        line_2[idx] += max(line_1[idx-1], line_1[idx-2])

    print(max(line_1[-1], line_2[-1]))