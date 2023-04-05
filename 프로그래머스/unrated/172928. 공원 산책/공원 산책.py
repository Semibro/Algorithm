def solution(park, routes):
    answer = []
    N = len(park)
    M = len(park[0])
    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                x, y = i, j
                break
    for i in routes:
        if i[0] == 'N':
            for j in range(1, int(i[2])+1):
                nx, ny = x-(1*j), y
                if 0 <= nx < N and 0 <= ny < M:
                    if park[nx][ny] == 'X':
                        break
                else:
                    break
            else:
                x, y = nx, ny
        elif i[0] == 'S':
            for j in range(1, int(i[2])+1):
                nx, ny = x+(1*j), y
                if 0 <= nx < N and 0 <= ny < M:
                    if park[nx][ny] == 'X':
                        break
                else:
                    break
            else:
                x, y = nx, ny
        elif i[0] == 'W':
            for j in range(1, int(i[2])+1):
                nx, ny = x, y-(1*j)
                if 0 <= nx < N and 0 <= ny < M:
                    if park[nx][ny] == 'X':
                        break
                else:
                    break
            else:
                x, y = nx, ny
        else:
            for j in range(1, int(i[2])+1):
                nx, ny = x, y+(1*j)
                if 0 <= nx < N and 0 <= ny < M:
                    if park[nx][ny] == 'X':
                        break
                else:
                    break
            else:
                x, y = nx, ny
    answer.extend([x, y])
    return answer