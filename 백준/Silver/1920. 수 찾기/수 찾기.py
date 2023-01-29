import sys

n = int(sys.stdin.readline())
check_lst = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
result_lst = list(map(int, sys.stdin.readline().split()))

for i in result_lst:
  if i in check_lst:
    print('1')
  else:
    print('0')