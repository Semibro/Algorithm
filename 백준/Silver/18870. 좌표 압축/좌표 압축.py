n = int(input())
default_list = list(map(int, input().split()))
in_list = list(set(default_list))
sort_list = sorted(in_list)
result_dict = {sort_list[i] : i for i in range(len(sort_list))}

for j in default_list:
    print(result_dict[j], end = ' ')