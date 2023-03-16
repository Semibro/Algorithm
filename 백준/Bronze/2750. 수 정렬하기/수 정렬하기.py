N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
print(*lst, sep='\n')