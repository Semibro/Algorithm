p, m = map(int, input().split())
teams = []

for _ in range(p):
    l, n = input().split()
    if len(teams) == 0:
        teams.append([(int(l), n)])
    else:
        idx = 0
        while idx <= len(teams):
            if idx == len(teams):
                teams.append([(int(l), n)])
                break
            if len(teams[idx]) < m and (teams[idx][0][0]-10 <= int(l) and teams[idx][0][0]+10 >= int(l)):
                teams[idx].append((int(l), n))
                break
            else:
                idx += 1

for i in range(len(teams)):
    teams[i].sort(key=lambda x: x[1])

    if len(teams[i]) == m:
        print('Started!')
        for level, nickname in teams[i]:
            print(level, nickname)
    else:
        print('Waiting!')
        for level, nickname in teams[i]:
            print(level, nickname)