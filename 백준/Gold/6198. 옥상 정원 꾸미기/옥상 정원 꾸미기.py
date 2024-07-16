N = int(input())
building, stack, answer = [], [], 0

for _ in range(N):
    building.append(int(input()))

for item in building:
    while stack and stack[-1] <= item:
        stack.pop()
    
    stack.append(item)

    answer += len(stack) - 1

print(answer)