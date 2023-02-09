X = int(input())
L = 1

while X > L:
    X -= L
    L += 1
    
if L % 2 == 0:
    num = X
    deno = L - X + 1
else:
    num = L - X + 1
    deno = X
    
print(num, '/', deno, sep = "")