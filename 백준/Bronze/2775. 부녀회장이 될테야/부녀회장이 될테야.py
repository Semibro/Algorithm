T = int(input())

for i in range(T):
  K = int(input())
  N = int(input())
  count = [j for j in range(1, N+1)]
  for k in range(K):
    for x in range(1, N):
      count[x] += count[x-1]
  print(count[-1])