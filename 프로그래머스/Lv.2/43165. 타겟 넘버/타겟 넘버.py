def solution(numbers, target):
    answer = 0
    def dfs(idx, num):
        if idx == len(numbers):
            if num == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, num+numbers[idx])
            dfs(idx+1, num-numbers[idx])
    dfs(0, 0)
    return answer