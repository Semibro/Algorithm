R, C, N = map(int, input().split())
x, y = 0, 0
if R % N:
    x += R//N + 1
else:
    x += R//N
    
if C % N:
    y += C//N  + 1
else:
    y += C//N
    
print(x*y)