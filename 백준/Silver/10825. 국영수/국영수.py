## 접근방법
# 국어를 기준으로 내림차순정렬
# 국어 점수가 같다면 영어 오름차순 정렬
# 국어, 영어 점수가 같다면 수학 내림차순 정렬
# 점수 다 같으면 이름 사전순

n = int(input())
student_list = []
for _ in range(n):
    student = list(input().split())
    student[1] = int(student[1])
    student[2] = int(student[2])
    student[3] = int(student[3])
    student_list.append(student)

# 선택정렬
# for i in range(n-1):
#     minIdx = i
#     for j in range(i+1, n):
#         if student_list[minIdx][1] < student_list[j][1]: # 국어 내림차순 정렬
#             student_list[j], student_list[minIdx] = student_list[minIdx], student_list[j]
#         elif student_list[minIdx][1] == student_list[j][1]: # 국어 점수가 같다면
#             if student_list[minIdx][2] > student_list[j][2]: # 영어 오름차순 정렬
#                 student_list[j], student_list[minIdx] = student_list[minIdx], student_list[j]
#             elif student_list[minIdx][2] == student_list[j][2]: # 국어, 영어 점수가 같다면
#                 if student_list[minIdx][3] < student_list[j][3]: # 수학 내림차순 정렬
#                     student_list[j], student_list[minIdx] = student_list[minIdx], student_list[j]
#                 elif student_list[minIdx][3] == student_list[j][3]: # 국어, 영어, 수학 점수가 같다면
#                     if student_list[minIdx][0] > student_list[j][0]: # 이름 사전순 정렬
#                         student_list[j], student_list[minIdx] = student_list[minIdx], student_list[j]
student_list.sort(key = lambda x: [-x[1], x[2], -x[3], x[0]])

for i in range(n):
    print(student_list[i][0])