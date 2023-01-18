num = int(input())
i = 1
result = []

while i <= 54:
    value = num-i
    compare_val = 0
    if value == 0:
        break
    for n in str(value):
        compare_val += int(n)
    if compare_val == i:
        result.append(value)
    i += 1

if len(result) == 0:
    print(0)
else: 
    print(min(result))