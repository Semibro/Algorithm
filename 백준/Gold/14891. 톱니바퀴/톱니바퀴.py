N = 4  # 일반화를 위한 변수
gear = [[0]*8] + [list(map(int, input())) for _ in range(N)]
K = int(input())
top = [0] * (N+1)

for _ in range(K):  # 회전 명령
    idx, dr = map(int, input().split())

    # [1] idx 톱니를 회전
    temp_lst = [(idx, 0)]

    # [2] idx 우측방향 처리 (같은 극성 나오면 종료)
    for i in range(idx+1, N+1):
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 => 회전후보 추가
        if gear[i-1][(top[i-1]+2)%8] != gear[i][(top[i]+6)%8]:
            temp_lst.append((i, (i-idx)%2))
        else:  # 같은 극성이면 종료
            break

    # [3] idx 좌측방향 처리
    for i in range(idx-1, 0, -1):
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 => 회전후보 추가
        if gear[i][(top[i]+2)%8] != gear[i+1][(top[i+1]+6)%8]:
            temp_lst.append((i, (idx-i)%2))
        else:  # 같은 극성이면 종료
            break

    # [4] 실제 회전 처리 (cw이면 top값을 -1)
    for i, rot in temp_lst:
        if rot == 0:  # idx톱니의 dr과 같은 방향
            top[i] = (top[i]-dr+8) % 8
        else:
            top[i] = (top[i]+dr+8) % 8

answer = 0
table = [0, 1, 2, 4, 8]

for i in range(1, N+1):
    answer += gear[i][top[i]] * table[i]

print(answer)