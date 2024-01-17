from collections import deque

def solution(progresses, speeds):
    answer = []
    total = len(speeds)
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    temp = 0
    while progresses:
        if progresses[0] >= 100:
            temp += 1
            progresses.popleft()
            speeds.popleft()
            continue
        else:
            if temp == 0:
                for i in range(len(speeds)):
                    progresses[i] += speeds[i]
            else:    
                answer.append(temp)
                temp = 0
    
    answer.append(total - sum(answer))
    return answer