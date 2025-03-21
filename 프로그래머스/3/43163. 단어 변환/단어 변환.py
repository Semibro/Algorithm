from collections import deque

def check_change_only_one_word(prev_word, next_word):
    n = len(prev_word)
    count = 0
    
    for i in range(n):
        if prev_word[i] != next_word[i]:
            count += 1
            if count > 1:
                return False
    
    return True


def bfs(start_index, target_word, words):
    queue = deque()
    visited = [0] * len(words)
    
    queue.append(start_index)
    visited[start_index] = 1
    
    while queue:
        current_index = queue.popleft()
        for next_index in range(len(words)):
            if visited[next_index] == 0 and check_change_only_one_word(words[current_index], words[next_index]):
                visited[next_index] = visited[current_index] + 1
                queue.append(next_index)
                
    if visited[words.index(target_word)] == 0:
        return 9876543210
    else:
        return visited[words.index(target_word)]
    

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 9876543210
    
    for i in range(len(words)):
        if check_change_only_one_word(begin, words[i]):
            count = bfs(i, target, words)
            answer = min(answer, count)
    
    return answer