A, B, C = map(int, input().split())
D = int(input())
beta = D // 60
ceta = D % 60
alpha = beta // 60
if C + ceta >= 60:
    B += (C + ceta) // 60
    C = (C + ceta) % 60
else:
    C += ceta
if B + beta >= 60:
    A += (B + beta) // 60
    B = (B + beta) % 60
else:
    B += beta
if A >= 24:
    A = A % 24

print(f'{A} {B} {C}')