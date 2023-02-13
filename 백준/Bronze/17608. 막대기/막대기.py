import sys

n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
    stack.append(int(sys.stdin.readline().rstrip()))
cnt = 0
dm = 0
for i in range(n-1, -1, -1):
    if dm < stack[i]:
        dm = stack[i]
        cnt += 1

print(cnt)