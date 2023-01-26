n = int(input())
if n == 4 or n == 7:
  print(-1)
else:

  five_lst = []
  three_lst = []
  result = []
  count = 0

  for i in range(int(n//5) + 1):
    five_lst.append(5 * i)
  for i in range(int(n//3) + 1):
    three_lst.append(3 * i)

  for i in range(len(three_lst)):
    for j in range(len(five_lst)):
      if five_lst[j] + three_lst[i] == n:
        result.append(j+i)

  print(min(result))