from collections import deque

n = int(input())
m = int(input())

friends = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

answer = 0
queue = deque()
queue.append((1, 0))
visited[1] = True

while queue:
    locate, value = queue.popleft()

    if value <= 2:
        answer += 1
    
    for friend in friends[locate]:
        if not visited[friend]:
            visited[friend] = True
            queue.append((friend, value+1))

print(answer-1)