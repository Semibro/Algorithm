N, TaeSu, P = map(int, input().split())
if N == 0:
    print(1)
else:
    points = list(map(int, input().split()))
    answer, count = 0, 0

    for point in points:
        if point > TaeSu:
            answer += 1
        elif point == TaeSu:
            count += 1
        else:
            break

    if answer + count + 1 <= P:
        print(answer + 1)
    else:
        print(-1)