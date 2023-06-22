N, M, K = map(int, input().split())
answer = 0
FX, BX = N-M, N-K

if M >= K:
    answer += K
else:
    answer += M
if FX >= BX:
    answer += BX
else:
    answer += FX

print(answer)