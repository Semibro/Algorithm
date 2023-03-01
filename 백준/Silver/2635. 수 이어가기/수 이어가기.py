N = int(input())
result = []
for i in range(1, N+1): # i는 두번째 수
    bin_lst = [N, i]
    if N-i < 0:
        result.extend([[len(bin_lst), bin_lst]])
    else:
        while True:
            if bin_lst[-2] - bin_lst[-1] < 0:
                break
            else:
                bin_lst.append(bin_lst[-2] - bin_lst[-1])
        result.extend([[len(bin_lst), bin_lst]])
result.sort()
print(result[-1][0])
print(*result[-1][1])