def solution(book_time):
    time = [0] * 1440
    for i in book_time:
        s = int(i[0][:2])*60 + int(i[0][3:])
        e = int(i[1][:2])*60 + int(i[1][3:])
        for j in range(s, min(e+10, 1440)):
            time[j] += 1
    answer = max(time)
    return answer