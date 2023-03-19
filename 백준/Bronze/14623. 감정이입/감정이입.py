B1 = input()
B2 = input()
a, b = 0, 0
for i in range(len(B1)-1, -1, -1):
    if B1[i] == '1':
        a += 2**(len(B1)-1-i)
for i in range(len(B2)-1, -1, -1):
    if B2[i] == '1':
        b += 2**(len(B2)-1-i)
c = a * b
res = format(c, 'b')
print(res)