# 팀 점수 = 상위 4명 주자의 점수 합
# 가장 낮은 점수를 얻은 팀이 우승
# 동점의 경우 5번째 주자가 빨리 들어온 팀이 우승
for _ in range(int(input())):
    N = int(input())
    TN = list(map(int, input().split()))  # Team Number
    Team = [[] for _ in range(201)]
    temp = []

    # 참가 가능한 팀 구하기
    for i in range(1, 201):
        if TN.count(i) >= 6:
            temp.append(i)

    # 팀 점수 구하기
    point = 1
    for number in TN:
        if number in temp and len(Team[number]) == 0:
            Team[number] = [number, point, 1]
            point += 1
        elif point > 1 and number in temp:
            Team[number][2] += 1
            if Team[number][2] == 5:
                Team[number].append(point)
            elif Team[number][2] < 5:
                Team[number][1] += point
            point += 1

    answer, min = 0, 9876543210
    for i in range(1, 201):
        if Team[i] and Team[i][1] < min:
            answer = i
            min = Team[i][1]
        elif Team[i] and Team[i][1] == min:
            if Team[answer][3] > Team[i][3]:
                answer = i

    print(answer)