tc = 0 # 출력에 사용될 변수
check = '{}' # 모양 확인을 위한 {}
while True:
    bracket = list(input()) # input
    tc += 1 # 케이스 한 번당 1씩 증가
    cnt = 0 # else문 안에서 while을 종료시키기 위한 변수
    result = 0 # 최종 출력값을 저장할 변수
    if '-' in bracket:
        break # '-'들어오면 break
    else:
        while True:
            if len(bracket) == 0: # {}모양이 다 있어서 길이가 0이되면 break
                break
            elif cnt == len(bracket)-1: # {}모양을 다 뺏는데 while이 작동할 수 있으므로 cnt를 증가시켜 len보다 1작다면 while작동 멈춤
                break
            else: # 위의 조건이 다 아니면 {}이 있으므로 {} pop
                for i in range(0, len(bracket)-1):
                    if bracket[i] + bracket[i+1] == check: # check와 비교하여 같으면 pop
                        bracket.pop(i)
                        bracket.pop(i) # i를 두번하는 이유 : pop(i)하는 순간 i+1의 위치가 i로 변경
                        cnt = 0
                        break
                    else:
                        cnt += 1 # 만약 check와 같은게 없을 때마다 cnt 증가
        for i in range(0, len(bracket), 2):
            if bracket[i] != check[0]: # for문을 2씩 증가하면서 최종적으로 나온 bracket에 check[0]과 비교
                result += 1 # 다르면 결과에 1추가
                if bracket[i+1] != check[1]: # bracket[i+1]과 check[1] 다르면 result += 1
                    result += 1
            else:
                if bracket[i+1] != check[1]: # bracket[i]는 같지만 i+1이 다르다면
                    result += 1 # 1추가
        print(f'{tc}. {result}')
