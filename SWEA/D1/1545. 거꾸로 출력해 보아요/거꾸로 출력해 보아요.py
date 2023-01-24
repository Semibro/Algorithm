n = int(input())
bin_list = []

for i in range(n, -1, -1):
  bin_list.append(i)

print(*bin_list)