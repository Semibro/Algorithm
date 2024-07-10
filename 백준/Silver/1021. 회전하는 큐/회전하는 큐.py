from collections import deque

N, M = map(int, input().split())
temp_list = list(map(int, input().split()))
queue = deque()

for i in range(1, N+1):
    queue.append(i)

count, temp = 0, 0

while temp < M:
    if temp_list[temp] == queue[0]:
        queue.popleft()
        temp += 1
    else:
        # 중앙값 구하기
        middle = len(queue) // 2

        if queue.index(temp_list[temp]) <= middle:
            t = queue.popleft()
            queue.append(t)
            count += 1
        else:
            t = queue.pop()
            queue.appendleft(t)
            count += 1

print(count)