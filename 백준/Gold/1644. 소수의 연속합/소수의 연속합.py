N = int(input())

if N == 1:
    print(0)
else:
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = False

    primes = []
    for i in range(2, N + 1):
        if sieve[i]:
            primes.append(i)

    if not primes:
        print(0)
    else:
        total, end, answer = 0, 0, 0

        for start in range(len(primes)):
            while end < len(primes) and total < N:
                total += primes[end]
                end += 1

            if total == N:
                answer += 1

            total -= primes[start]

        print(answer)