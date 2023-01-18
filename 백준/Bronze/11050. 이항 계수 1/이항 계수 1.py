N, K = map(int, input().split())

def factorial(n):
  ans = 1
  for i in range(2, n+1):
    ans *= i
  return ans

def bino_coef_factorial(n, k):
  return factorial(n) // factorial(k) // factorial(n-k)

print(bino_coef_factorial(N, K))