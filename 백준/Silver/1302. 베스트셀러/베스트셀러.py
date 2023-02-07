n = int(input()) # input
book_list = [] # 책을 받아 저장할 리스트
result_dict = {} # Key : 책 / Value : 책의 개수
result_list = [] # 만약 max값이 같다면 sort를 진행하기 위한 리스트

for _ in range(n): # 책을 입력받아 리스트에 저장
    book = input()
    book_list.append(book)

for j in set(book_list): # set을 이용해 책을 Key에 하나만 저장하고 count값을 value로 저장
    result_dict[j] = int(book_list.count(j))

max_value = max(result_dict.values()) # value 중 최고 값 저장
for i in result_dict: # dict를 돌면서 max값과 같은 값을 리스트에 저장
    if result_dict[i] == max_value:
        result_list.append(i)

result_list.sort() # 리스트를 정렬
print(result_list[0])