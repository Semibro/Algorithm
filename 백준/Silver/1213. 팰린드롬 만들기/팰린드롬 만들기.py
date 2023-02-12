## 접근방법
# 문자는 홀수 개수일 경우가 최대 1
# 짝수개만 있을 때 / 홀수개가 1개 포함되어 있을 때
# 홀수개 중 하나는 무조건 중간에 위치 (int(len(wor)//2) +1)
# 짝수개만 있다면 문자가 빠른것부터 /2 한거를 append
# 리스트보다 문자열

word = input()
bin_dict = dict()
for i in word:
    if i in bin_dict:
        bin_dict[i] += 1
    else:
        bin_dict[i] = 1

# 홀수개인 값 찾기
holsu_cnt = 0
for k, v in bin_dict.items():
    if v % 2 != 0:
        holsu_cnt += 1

# 사전순 정렬
sort_dict = dict(sorted(bin_dict.items()))

# 홀수개인 개수가 2개 이상이면 회문이 불가능
result_list = []
holsu = []
if holsu_cnt >= 2:
    print("I'm Sorry Hansoo")
else: # 회문이 가능한 상황
    if holsu_cnt == 0: # 짝수개만 있음
        for k, v in sort_dict.items(): # for문으로 딕셔너리 값 가져옴
            for i in range(int(v/2)): # value값을 2로 나눠서 회문 절반 append (AABB 중 AB)
                result_list.append(k)
        for i in range(len(result_list)-1, -1, -1): # 저장된 리스트를 거꾸로 돌면서 다시 append (ABBA)
            result_list.append(result_list[i])
        print(''.join(result_list))
    else:
        for k, v in sort_dict.items():
            if v % 2 != 0:
                holsu.append(k)
        for k, v in sort_dict.items():
            for i in range(int(v/2)):
                result_list.append(k)
        result_list = result_list+holsu
        for i in range(len(result_list)-2, -1, -1):
            result_list.append(result_list[i])
        print(''.join(result_list))