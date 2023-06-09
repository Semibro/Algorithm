N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# [1] 집, 치킨집 좌표
home, chicken = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
chicken_len = len(chicken)

# [2] 백트래킹 (최솟값 구하기)
answer = 9876543210  # 최소를 구하기 위한 최댓값 생성

def cal(temp_lst):
    # 모든 집과 temp_lst의 치킨집 중 최소값의 누적값 구하기
    result = 0
    for i, j in home:  # 집 좌표 꺼내기
        min_value = 9876543210
        for k, l in temp_lst:
            min_value = min(min_value, abs(i-k)+abs(j-l))
        result += min_value
    return result


def dfs(n, temp_lst):
    global answer
    if n == chicken_len:  # 백트래킹 종료조건 : 모든 치킨집의 폐업여부를 결정
        if len(temp_lst) == M:  # 치킨집이 M개일때
            answer = min(answer, cal(temp_lst))
        return
    # 유지하는 경우
    dfs(n+1, temp_lst+[chicken[n]])
    # 폐업하는 경우
    dfs(n+1, temp_lst)

dfs(0, [])
print(answer)