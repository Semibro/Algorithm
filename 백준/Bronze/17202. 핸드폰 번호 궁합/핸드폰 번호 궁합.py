def phone(str_num):
    if len(str_num) == 2:
        print(str_num)
        return
    else:
        bin = ''
        for i in range(0, len(str_num)-1):
            if int(str_num[i]) + int(str_num[i+1]) >= 10:
                a = str(int(str_num[i]) + int(str_num[i+1]))
                bin += a[1]
            else:
                bin += str(int(str_num[i]) + int(str_num[i+1]))
        phone(bin)

A = input()
B = input()
bin_str = ''
for i in range(0, 8):
    for j in (i, 8):
        bin_str += A[i]
        bin_str += B[j]
        break
phone(bin_str)