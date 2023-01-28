bin_list = []
for i in range(5):
  lst = list(map(int, input().split()))
  total = 0
  for j in lst:
    total += j
  bin_list.append(total)

print(f'{bin_list.index(max(bin_list)) + 1} {max(bin_list)}')