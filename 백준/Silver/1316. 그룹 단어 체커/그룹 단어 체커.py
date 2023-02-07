n = int(input()) # input
count = n # 그룹단어 체크를 위해 카운트에서 하나씩 뺄 예정

for i in range(n):
    word = input()
    for j in range(len(word) - 1):
        if word[j] == word[j+1]: # 연속되는지 체크 / 연속되면 pass
            pass
        elif word[j] in word[j+1:]: # 연속이 아니라면 다음 단어부터 해당 단어가 있는지 확인
            count -= 1 # 단어가 있다면 count에서 -1
            break
print(count)