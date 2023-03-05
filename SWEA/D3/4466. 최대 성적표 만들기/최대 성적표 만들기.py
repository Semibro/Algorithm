for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    grade = list(map(int, input().split()))
    grade.sort(reverse=True)
    print(f'#{tc} {sum(grade[:K])}')