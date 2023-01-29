import sys

n = int(sys.stdin.readline())
result = []

for i in range(n):
  num = int(sys.stdin.readline())
  if num == 0:
    result.pop(-1)
  else:
    result.append(num)

rlt_sum = 0
for i in result:
  rlt_sum += i

print(rlt_sum)