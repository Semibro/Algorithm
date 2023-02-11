## 접근방법
# '.'을 만나면 cnt +1 / X를 만나면 cnt = 0으로 초기화
# 함수로 정의해서 cnt가 2이상이면 True 리턴

def checker(lst):
    cnt = 0 # '.'의 개수
    r_cnt = 0 # '.'의 개수가 2개 연속일 때 +1
    for i in lst:
        if i == '.': # '.'을 만나면 +1
            cnt += 1
        else: # 'X'를 만났을 때
            if cnt >= 2: # 누울 수 있는 자리면
                r_cnt += 1 # return_count값에 +1
                cnt = 0 # cnt 초기화
            else: # 아니면
                cnt = 0 # 그냥 초기화
    if cnt >= 2: # 'X'를 못만나면 return_count가 0이므로 ('X'를 한번이라도 만나고 벽을 못만날 경우도 추가)
        return r_cnt + 1 # return_count값에 1추가
    else: # 아니면 그냥 출력
        return r_cnt


n = int(input())
room = [list(input()) for _ in range(n)]

# 가로 확인
row_count = 0
for i in range(len(room)):
    row_count += checker(room[i])

# 세로 확인
# NXN 배열이므로 가로 세로 뒤집어 사용
for i in range(n):
    for j in range(i):
        room[i][j], room[j][i] = room[j][i], room[i][j]

col_count = 0
for i in range(len(room)):
    col_count += checker(room[i])

print(row_count, col_count)