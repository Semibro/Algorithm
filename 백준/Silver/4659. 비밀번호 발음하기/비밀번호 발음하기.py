moum = ('a', 'e', 'i', 'o', 'u')
while True:
    tc = input()
    if tc == 'end':
        break
    else:
        count = 0
        cnt_m = 0
        cnt_j = 0
        for i in range(len(tc)):
            if tc[i] in moum:
                count += 1
                cnt_m += 1
                cnt_j = 0
            else:
                cnt_m = 0
                cnt_j += 1
            if i < len(tc)-1:
                if tc[i] == tc[i+1]:
                    if (tc[i] == 'e' and tc[i+1] == 'e') or (tc[i] == 'o' and tc[i+1] == 'o'):
                        pass
                    else:
                        print(f'<{tc}> is not acceptable.')
                        break
            if cnt_m >= 3 or cnt_j >= 3:
                print(f'<{tc}> is not acceptable.')
                break
        else:
            if count >= 1:
                print(f'<{tc}> is acceptable.')
            else:
                print(f'<{tc}> is not acceptable.')