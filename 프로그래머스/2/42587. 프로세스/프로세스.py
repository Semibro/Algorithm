from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    priorities = deque(priorities)
    for i in range(len(priorities)):
        queue.append(i)
        
    while priorities:
        if priorities[0] == max(priorities):
            answer += 1
            priorities.popleft()
            temp = queue.popleft()
            if temp == location:
                return answer
        else:
            queue.append(queue.popleft())
            priorities.append(priorities.popleft())
    