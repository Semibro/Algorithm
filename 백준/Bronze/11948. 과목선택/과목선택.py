A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

max_1 = max(A+B+C, A+B+D, B+C+D, A+C+D)
max_2 = max(E, F)
print(max_1+max_2)