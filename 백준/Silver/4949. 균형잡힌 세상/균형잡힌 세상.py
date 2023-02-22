while True:
    lst = list(input())
    if len(lst) == 1 and lst[0] == '.':
        break
    else:
        stack = []
        for i in lst:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0:
                    print('no')
                    break
                else:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        print('no')
                        break
            elif i == ']':
                if len(stack) == 0:
                    print('no')
                    break
                else:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        print('no')
                        break
            elif i == '.':
                if len(stack) == 0:
                    print('yes')
                    break
                else:
                    print('no')
                    break
            else:
                pass