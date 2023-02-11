## 접근방식 ##
# 입력받은 리스트롤 sort한다.
# 커트라인으로 k를 사용 (ex. list[-k])

n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort(reverse=True)
# # 버블정렬
# for i in range(5-1, 0, -1):
#     for j in range(i):
#         if x[j] < x[j+1]:
#             x[j], x[j+1] = x[j+1], x[j]

print(x[k-1])