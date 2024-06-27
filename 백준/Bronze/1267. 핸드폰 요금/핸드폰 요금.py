N = int(input())
time = list(map(int, input().split()))
Y, M = 0, 0

for item in time:
    Y += (item//30 + 1) * 10
    M += (item//60 + 1) * 15
if M == Y:
    print("Y M", Y)
elif M < Y:
    print("M", M)
else:
    print("Y", Y)