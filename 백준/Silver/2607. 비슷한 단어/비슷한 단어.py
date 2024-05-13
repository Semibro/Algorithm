N = int(input())
word = list(input())
answer = 0
for _ in range(N-1):
    check = input()
    words = word[:]
    cnt = 0

    for c in check:
        if c in words:
            words.remove(c)
        else:
            cnt += 1
    
    if cnt <= 1 and len(words) <= 1:
        answer += 1

print(answer)