from collections import deque

L = int(input())

# -: 백스페이스, <: 좌로 이동, >: 우로 이동
for _ in range(L):
    test_string = input()
    queue1, queue2 = deque(), deque()

    for item in test_string:
        if item == '<':
            if queue1:
                queue2.appendleft(queue1.pop())
        elif item == '>':
            if queue2:
                queue1.append(queue2.popleft())
        elif item == '-':
            if queue1:
                queue1.pop()
        else:
            queue1.append(item)

    answer1, answer2 = ''.join(queue1), ''.join(queue2)

    print(answer1+answer2)