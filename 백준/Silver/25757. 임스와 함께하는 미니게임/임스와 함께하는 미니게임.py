N, game = input().split()

lst = set()
for _ in range(int(N)):
    lst.add(input())

if game == 'Y':
    print(len(lst))
elif game == 'F':
    print(len(lst)//2)
else:
    print(len(lst)//3)