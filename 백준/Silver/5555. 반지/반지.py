## 접근방법
# input으로 받은 문자열 중 0,1,2번 문자열을 문자열 뒤에 추가
# 그러면 반지처럼 연결된 형태로 생각 가능

check = input()
n = int(input())
word_list = []
for _ in range(n):
    word_list.append(input())

for i in range(n):
    word_list[i] = word_list[i] + word_list[i][0:len(check)]

result_count = 0
for i in range(n):
    for j in range(len(word_list[i])-len(check)+1):
        if word_list[i][j:j+len(check)] == check:
            result_count += 1
            break

print(result_count)