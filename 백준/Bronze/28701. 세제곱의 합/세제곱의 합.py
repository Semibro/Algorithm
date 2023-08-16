N = int(input())

x, y = 0, 0

for i in range(1, N+1):
    x += i
    y += (i**3)
    
print(x)
print(x**2)
print(y)