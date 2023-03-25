N = int(input())
arr = [[0] * (N+2) for _ in range(N+2)]
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
check_2 = []
for _ in range(N**2):
    student_lst = list(map(int, input().split()))
    check_2.append(student_lst)
    student = student_lst[0]
    student_like = student_lst[1:]
    check = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 0:
                like_cnt = 0
                bin_cnt = 0
                for d in delta:
                    si, sj = i+d[0], j+d[1]
                    if 1<=si<N+1 and 1<=sj<N+1:
                        if arr[si][sj] == 0:
                            bin_cnt += 1
                        if arr[si][sj] in student_like:
                            like_cnt += 1
                check.append((like_cnt, bin_cnt, i, j))
    check.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    arr[check[0][2]][check[0][3]] = student

check_2.sort(key=lambda x: x[0])
result = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        cnt = 0
        for d in delta:
            si, sj = i+d[0], j+d[1]
            if arr[si][sj] in check_2[arr[i][j]-1][1:]:
                cnt += 1
        if cnt != 0:
            result += 10**(cnt-1)

print(result)

## 반례
# 시작하자마자 틀리다고 나와서 뭐가 틀린지 몰라 질문게시판 찾아봄.
# 그리고 그 곳에서 힌트를 얻음
# 3
# 7 9 3 8 2 
# 5 7 3 8 6
# 3 5 2 4 9
# 9 6 8 3 4
# 8 5 3 1 6
# 6 3 8 5 4
# 2 6 4 8 7
# 1 8 3 4 5
# 4 7 9 3 8
# 위의 케이스의 경우 원래 코드에서 151.2가 나옴;;
# 소수점이 왜나오나 고민하다가 찾아냄..
# cnt가 0이면 10**-1로 문제가 생긴다.