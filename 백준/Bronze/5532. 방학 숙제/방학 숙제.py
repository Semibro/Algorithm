L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A%C:
    a = A//C+1
else:
    a = A//C
if B%D:
    b = B//D+1
else:
    b = B//D
print(L - max(a, b))