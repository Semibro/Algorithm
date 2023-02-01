N = int(input())

word = []

for i in range(N):
  value = input()
  word.append((len(value), value)) # 단어의 길이와 단어를 함께 튜플 형태로 리스트에 저장
word = list(set(word)) # 중복 제거를 위한 set 형태 후 다시 리스트형태로 저장
word.sort() # 길이에 대한 정보가 먼저 sort된 후, 글자에 대해 sort진행
for word_len, word_str in word: # 길이와 글자에 대해 for문 작동 후, 글자만 추출
  print(word_str)