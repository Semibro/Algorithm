N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0
for i in A:
    total += 1
    i -= B
    if i <= 0:
        pass
    else:
        total += i // C
        if i % C:
            total += 1

print(total)