import sys
n = int(sys.stdin.readline())
result_list = []
for _ in range(n):
    result_list.append(int(sys.stdin.readline()))
result_list.sort(reverse=True)
for i in range(n):
    print(result_list[i])