tc = 0 # 출력에 사용될 변수
check = '{}'
while True:
    bracket = list(input()) # input
    tc += 1 # 케이스 한 번당 1씩 증가
    cnt = 0
    result = 0
    if '-' in bracket:
        break # '-'들어오면 break
    else:
        while True:
            if len(bracket) == 0:
                break
            elif cnt == len(bracket)-1:
                break
            else:
                for i in range(0, len(bracket)-1):
                    if bracket[i] + bracket[i+1] == check:
                        bracket.pop(i)
                        bracket.pop(i)
                        cnt = 0
                        break
                    else:
                        cnt += 1
        for i in range(0, len(bracket), 2):
            if bracket[i] != check[0]:
                result += 1
                if bracket[i+1] != check[1]:
                    result += 1
            else:
                if bracket[i+1] != check[1]:
                    result += 1
        print(f'{tc}. {result}')