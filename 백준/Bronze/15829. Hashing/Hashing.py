n = int(input())
alpha = input()
result = 0
for i in range(n):
    result += ((ord(alpha[i])-96) * (31**i)) % 1234567891
print(result)