hour, minute = map(int, input().split())
timer = int(input())

hour += timer // 60   # 시간은 60분으로 나눈 몫이 더해진다.
minute += timer % 60  # 분은 60분으로 나눈 나머지가 더해진다.

if minute >= 60:  # 만약 60분으로 나눈 나머지가 더해진 후의 값이 60분 보다 많다면
                  # 즉, 1시간이 추가된다면
  hour += 1       # 1시간 추가
  minute -= 60    # 60분을 빼서 나머지 분 저장

if hour >= 24:    # 24시간이 되면 0으로 바꿔줘야 하므로 조건을 옆에와 같이 걸고
  hour -= 24      # 시간에서 24을 빼서 0으로 바뀔 수 있게 저장

print(hour, minute)
