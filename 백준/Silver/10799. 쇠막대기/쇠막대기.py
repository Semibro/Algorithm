razer = input()
result, stack = 0, []

for i in range(len(razer)):
    if razer[i] == '(':
        stack.append(i)
    else:
        if razer[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)