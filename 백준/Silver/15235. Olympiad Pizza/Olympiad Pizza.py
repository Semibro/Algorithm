from collections import deque

N = int(input())
# enumerate는 index 생성
queue = deque(enumerate(list(map(int, input().split()))))
answer = [0] * N
cnt = 0

while queue:
    idx, left = queue.popleft()
    cnt += 1
    answer[idx] = cnt
    left -= 1
    if left != 0:
        queue.append((idx, left))

print(" ".join(str(answer[i]) for i in range(N)))