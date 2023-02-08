n = input().split('-')
minus_list = []
for i in n:
    total = 0
    plus = i.split('+')
    for j in plus:
        total += int(j)
    minus_list.append(total)
first = minus_list[0]
for k in range(1, len(minus_list)):
    first -= minus_list[k]
print(first)