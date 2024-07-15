moonjayeol = input()
stack, answer, temp = [], 0, 1

for idx in range(len(moonjayeol)):
    if moonjayeol[idx] == '(':
        stack.append(moonjayeol[idx])
        temp *= 2
    elif moonjayeol[idx] == '[':
        stack.append(moonjayeol[idx])
        temp *= 3
    elif moonjayeol[idx] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if moonjayeol[idx-1] == '(':
            answer += temp
        temp = temp // 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if moonjayeol[idx-1] == '[':
            answer += temp
        temp = temp // 3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)