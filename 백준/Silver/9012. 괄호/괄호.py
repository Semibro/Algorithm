n = int(input())

for i in range(n):
    count = 0 # (를 count
    vps = input()
    for j in vps: # vps안에 (가 있으면 +1 아니면 -1
        if j == '(':
            count += 1
        else:
            count -= 1
            if count < 0: # count가 음수로 가는 경우에 vps를 만족하지 못함
                break
    if count == 0: # count가 0이 아니면 vps만족하지 못하므로
        print('YES')
    else:
        print('NO')