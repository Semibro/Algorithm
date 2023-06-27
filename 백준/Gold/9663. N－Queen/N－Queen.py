import sys
input = sys.stdin.readline

N = int(input())
answer = 0
col_visited = [0] * N  # 열 체크를 위한 리스트
right_up_visited = [0] * (2*N)  #오른쪽 위로 올라가는 대각선 체크를 위한 리스트
left_up_visited = [0] * (2*N)  #왼쪽 위로 올라가는 대각선 체크를 위한 리스트

def dfs(n):
    global answer
    if n == N:  # N행까지 갔다면 종료 (성공했다는 의미)
        answer += 1
        return
    for y in range(N):
        if col_visited[y] == right_up_visited[n+y] == left_up_visited[n-y] == 0:
            col_visited[y] = right_up_visited[n+y] = left_up_visited[n-y] = 1
            dfs(n+1)
            col_visited[y] = right_up_visited[n+y] = left_up_visited[n-y] = 0
            
dfs(0)
print(answer)