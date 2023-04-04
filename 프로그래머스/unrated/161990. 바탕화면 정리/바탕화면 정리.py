def solution(wallpaper):
    answer = []
    N, M = len(wallpaper), len(wallpaper[0])
    #
    for i in range(N):
        if len(answer) == 1:
            break
        for j in range(M):
            if wallpaper[i][j] == '#':
                answer.append(i)
                break
    ##
    for i in range(M):
        if len(answer) == 2:
            break
        for j in range(N):
            if wallpaper[j][i] == '#':
                answer.append(i)
                break
    ###
    for i in range(N-1, -1, -1):
        if len(answer) == 3:
            break
        for j in range(M):
            if wallpaper[i][j] == '#':
                answer.append(i+1)
                break
    ####
    for i in range(M-1, -1, -1):
        if len(answer) == 4:
            break
        for j in range(N):
            if wallpaper[j][i] == '#':
                answer.append(i+1)
                break
                
    return answer