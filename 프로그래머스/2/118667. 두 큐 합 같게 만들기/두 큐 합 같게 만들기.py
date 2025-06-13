from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    total = sum(q1) + sum(q2)
    
    # 합이 홀수일 경우, 절대 나눌 수 없음
    if total % 2 != 0:
        return -1
    
    target = total // 2
    sum1, sum2 = sum(q1), sum(q2)
    
    # 각 원소가 q1, q2에 한번씩 가면 모든 상태를 다 확인한 것이므로 3번 이동은 이미 확인한 상태여서 3으로 설정
    max_count = max(len(q1), len(q2)) * 3   # 무한루프 방지
    count = 0
    p1, p2 = 0, 0
    
    while count <= max_count:
        if sum1 == target:
            return count
        elif sum1 > target:
            temp = q1.popleft()
            sum1 -= temp
            q2.append(temp)
            sum2 += temp
        else:
            temp = q2.popleft()
            sum2 -= temp
            q1.append(temp)
            sum1 += temp
        count += 1
        
    return -1