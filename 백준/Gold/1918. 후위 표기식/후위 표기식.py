middle = input()
stack = []
result = ''

for i in middle:
    if i.isalpha():
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i =='/':
            while True:
                if len(stack) == 0:
                    break
                elif stack[-1] == '*' or stack[-1] == '/':
                    result += stack.pop()
                else:
                    break
            stack.append(i)
        elif i == '+' or i == '-':
            while True:
                if len(stack) == 0:
                    break
                elif stack[-1] == '(':
                    break
                else:
                    result += stack.pop()
            stack.append(i)
        else:
            while True:
                if len(stack) == 0:
                    break
                elif stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    result += stack.pop()

while stack:
    result += stack.pop()
print(result)