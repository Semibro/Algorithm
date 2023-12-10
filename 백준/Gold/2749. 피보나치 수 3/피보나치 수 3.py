n = int(input())
fibo = [0, 1]
mod = 1000000
# 피사노 주기를 활용하여 계산
# 피사노 주기에 따라 나누는 값(M = 10^k(k>2))의 -1승을 15에 곱한다.
# 15 * 10^(k-1)
fisano = 15 * (mod // 10)

if n == 0:
    print(fibo[0])
elif n == 1:
    print(fibo[1])
else:
    for i in range(2, fisano):
        fibo.append(fibo[i-1] + fibo[i-2])
        fibo[i] = fibo[i] % mod
    print(fibo[n%fisano])