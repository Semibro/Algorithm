n = int(input())
bin_list = []

for i in range(n):
  x, y = map(int, input().split())
  bin_list.append((x, y))

bin_list.sort()
for j in range(n):
  print(*bin_list[j])