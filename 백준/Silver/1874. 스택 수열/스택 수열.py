n = int(input())
ans = []
for _ in range(n):
    ans.append(int(input()))
result = []
stack = [0]
Idx = 0
value = 0
switch = 0
while True:
    if Idx == n:
        switch = 1
        break
    else:
        if stack[-1] < ans[Idx]:
            value += 1
            stack.append(value)
            result.append('+')
        elif stack[-1] == ans[Idx]:
            Idx += 1
            stack.pop()
            result.append('-')
        else:
            break
if switch == 0:
    print('NO')
else:
    for i in result:
        print(i)