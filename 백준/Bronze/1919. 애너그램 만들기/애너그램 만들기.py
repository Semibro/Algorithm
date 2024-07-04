one = input()
two = input()
answer = 0

# a ~ z : 97 ~ 123
for idx in range(97, 123):
    answer += abs(one.count(chr(idx)) - two.count(chr(idx)))

print(answer)