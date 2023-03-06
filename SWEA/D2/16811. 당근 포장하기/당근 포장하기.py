for tc in range(1, int(input())+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    minv = 1001
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                A = i + 1
                B = j - i
                C = N - j - 1
                if A*B*C != 0:
                    if A <= N//2 and B <= N//2 and C <= N//2:
                        if minv > max(A, B, C) - min(A, B, C):
                            minv = max(A, B, C) - min(A, B, C)
    if minv == 1001:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {minv}')