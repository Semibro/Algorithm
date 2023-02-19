n = int(input())
alpha = input()
result = 0
for i in range(n):
    result += (ord(alpha[i])-96) * (31**i)
print(result % 1234567891)
