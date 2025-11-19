N = int(input())
A = list(map(int, input().split()))

if len(A) % 2 == 0:
    print("Alice")
else:
    print("Bob")