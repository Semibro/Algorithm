n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.sort()
a, b = 0, n-1
answer = 0

while a < b:
    if lst[a] + lst[b] > x:
        b -= 1
    elif lst[a] + lst[b] < x:
        a += 1
    else:
        answer += 1
        a += 1
        b -= 1

print(answer)