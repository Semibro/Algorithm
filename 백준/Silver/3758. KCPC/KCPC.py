T = int(input())  # T개의 테스트

for _ in range(T):
    # n: 팀의 개수, k: 문제의 개수, t: 팀의 ID, m: 로그 엔트리의 개수
    n, k, t, m = map(int, input().split())
    # 팀별 제출횟수
    # team_point[0]: 팀별 카운트 / team_point[-2]: 팀별 총합 / team_point[-1]: 팀별 제출순서
    team_point = [[0 for _ in range(k+1)] for _ in range(n+1)]
    submit_count = [0 for _ in range(n+1)]
    last_time = [0 for _ in range(n+1)]

    

    for time in range(m):
        # i: 팀 ID, j: 문제 번호, s: 획득한 점수
        i, j, s = map(int, input().split())
        team_point[i][j] = max(team_point[i][j], s)
        submit_count[i] += 1
        last_time[i] = time

    # 팀별 점수 표
    teams = []
    for i in range(1, n+1):
        teams.append((sum(team_point[i]), submit_count[i], last_time[i], i))
    
    teams.sort(key= lambda x: (-x[0], x[1], x[2]))

    for i in range(n):
        if teams[i][3] == t:
            print(i+1)