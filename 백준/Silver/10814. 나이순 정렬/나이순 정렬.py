n = int(input())
bin_list = []

for i in range(n):
  age, name = input().split()
  age = int(age)
  bin_list.append((age, name))

bin_list.sort(key = lambda x : x[0])

for j in bin_list:
  print(j[0], j[1])