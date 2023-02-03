n = int(input())
mem_lst = [] # 멤버를 저장할 리스트 생성
for _ in range(n):
    age, name = input().split() # 나이와 이름 input으로 받음
    age = int(age) # 나이를 int형으로 변경
    mem_lst.append((age, name)) # 리스트에 저장
mem_lst.sort(key = lambda x: x[0]) # 람다식을 사용해서 나이순으로 정렬
for i in mem_lst:
    print(i[0], i[1])