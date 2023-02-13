word = input()
stack = []
for i in range(len(word)):
    stack.append(word[i])
    if len(stack) >= 4:
        if stack[-1:-5:-1] == ['P', 'A', 'P', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()
if stack == ['P']:
    print('PPAP')
else:
    print('NP')