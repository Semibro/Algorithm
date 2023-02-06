n = int(input())
hw_lst = []
for i in range(n):
    h, w = map(int, input().split())
    hw_lst.extend([0, h, w])
for j in range(0, len(hw_lst), 3):
    for k in range(0, len(hw_lst), 3):
        if hw_lst[j+1] < hw_lst[k+1]:
            if hw_lst[j+2] < hw_lst[k+2]:
                hw_lst[j] += 1

for l in range(0, len(hw_lst), 3):
    print(f'{hw_lst[l] + 1}', end=' ')