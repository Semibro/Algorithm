n = int(input())
book_list = []
result_dict = {}
max_list = []
result_list = []

for _ in range(n):
    book = input()
    book_list.append(book)

for j in set(book_list):
    result_dict[j] = int(book_list.count(j))

max_value = max(result_dict.values())
for i in result_dict:
    if result_dict[i] == max_value:
        result_list.append(i)

result_list.sort()
print(result_list[0])