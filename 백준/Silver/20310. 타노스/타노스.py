S = input()
zero, one = int(S.count('0'))//2, int(S.count('1'))//2
print('0'*zero + '1'*one)