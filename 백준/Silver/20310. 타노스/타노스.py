S = list(input())
zero, one = int(S.count('0'))//2, int(S.count('1'))//2

cnt = 0
for i in S:
    if i == '1':
        S.remove(i)
        cnt += 1
        if cnt == one:
            break

cnt = 0
S = S[::-1]
for i in S:
    if i == '0':
        S.remove(i)
        cnt += 1
        if cnt == zero:
            break

for i in S[::-1]:
    print(i, end="")