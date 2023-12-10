N, K = map(int, input().split())
MOD = 1000000007

def binomial_coefficient(n, k):
    fact = [1] * (n+1)

    # 팩토리얼
    for i in range(1, n+1):
        fact[i] = (fact[i-1] * i) % MOD

    # 모듈러 연산을 사용한 역원 계산
    def mod_inverse(x):
        return pow(x, MOD-2, MOD)

    num = fact[n]
    denominator = (fact[k] * fact[n-k]) % MOD

    return (num * mod_inverse(denominator)) % MOD

print(binomial_coefficient(N, K))