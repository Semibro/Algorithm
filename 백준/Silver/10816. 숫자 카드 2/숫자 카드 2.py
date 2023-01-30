import sys

n = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
card_dict = {} # 시간복잡도 해결을 위해 리스트말고 딕셔너리 사용 (딕셔너리 시간복잡도 O(1))
for i in card_list: # 딕셔너리에 Key로는 card_list값을 사용하고 value로는 card_list안의 요소의 개수를 사용
    if i in card_dict.keys():
        card_dict[i] += 1
    else:
        card_dict[i] = 1

m = int(sys.stdin.readline())
answer_list = list(map(int, sys.stdin.readline().split()))
result_list = []

for j in answer_list:
    try: # try-except문으로 j가 딕셔너리 안에 없다면 0추가
        result_list.append(card_dict[j]) # j가 딕셔너리 안에 있다면 결과 리스트에 추가
    except:
        result_list.append(0)

print(*result_list)