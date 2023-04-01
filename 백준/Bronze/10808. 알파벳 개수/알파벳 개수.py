S = input()
result = [0] * 26
for i in S:
    result[ord(i)-97] += 1
print(*result)