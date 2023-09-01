n = int(input())
lst = list(map(int, input().split()))

good, bad = 0, 0

for i in range(n):
    if lst[i] % 2 == 0:
        good += 1
    else:
        bad += 1
        
if good > bad:
    print('Happy')
else:
    print('Sad')