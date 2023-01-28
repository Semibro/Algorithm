n = int(input())
lst = list(map(int, input().split()))
max = lst[0]
min = lst[0]

for i in lst[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)