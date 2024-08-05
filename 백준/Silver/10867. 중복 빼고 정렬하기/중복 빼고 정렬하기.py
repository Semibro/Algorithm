N = int(input())
lst = list(set(list(map(int, input().split()))))
lst.sort()

for i in lst:
    print(i, end=" ")