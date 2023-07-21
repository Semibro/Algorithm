A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A < B and B < C and C < D:
    print('Fish Rising')
elif A > B and B > C and C > D:
    print('Fish Diving')
elif A == B and B == C and C == D:
    print('Fish At Constant Depth')
else:
    print('No Fish')