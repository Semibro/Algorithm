T = int(input())

for i in range(0, T):
  H, W, N = map(int, input().split())

  if H == 1:
    print(100 + N)
  elif N % H == 0:
    print(H * 100 + (N//H))
  else:
    print((N % H)*100 + ((N//H)+1))