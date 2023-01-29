n, k = map(int, input().split())
result = [] # 요세푸스 순열을 저장할 빈 리스트
lst = [] # 1번부터 n번까지의 사람을 저장할 리스트
idx = 0 # 제거할 사람의 index

for i in range(1, n+1):
  lst.append(i) # 1번부터 n번까지의 리스트 생성성

for _ in range(n):
  idx += k - 1 # index로 계산해야하므로 k-1로 k번째 사람 제거거
  if idx >= len(lst): # index값이 리스트 밖으로 나가면 나머지로 다시 리스트 안의 들어옴
    idx = idx % len(lst)
  result.append(str(lst.pop(idx))) # index에 맞게 사람을 pop을 통해 제거 후, 결과 리스트에 추가가

print(f'<{", ".join(result)[:]}>') # join명령어 : ','.join([a, b, c])를 하면 a,b,c로 출력력