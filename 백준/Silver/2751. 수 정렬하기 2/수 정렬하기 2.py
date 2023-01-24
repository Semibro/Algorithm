import sys
n = int(sys.stdin.readline()) # 시간초과 이슈로 인한 sys 사용용
bin_list = []              # 정렬에 사용할 빈 리스트 생성

for i in range(n):
  number = int(sys.stdin.readline())
  bin_list.append(number)  # for문을 활용해 숫자를 입력받고 빈 리스트에 저장

bin_list.sort()            # sort를 빈 리스트를 오름차순 정렬렬

for i in range(n):
  print(bin_list[i])       # for문을 활용해 출력
