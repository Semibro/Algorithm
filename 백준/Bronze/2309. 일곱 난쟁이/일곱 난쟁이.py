nanjaeng2 = []
for _ in range(9):
    a = int(input())
    nanjaeng2.append(a)

subsets = [[]]
for i in nanjaeng2:
    length = len(subsets)
    for j in range(length):
        subsets.append(subsets[j] + [i])

for i in subsets:
    if len(i) == 7 and sum(i) == 100:
        result = i
result.sort()
for i in result:
    print(i)