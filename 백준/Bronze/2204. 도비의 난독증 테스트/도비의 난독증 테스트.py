while True:
    n = int(input())
    if n == 0:
        break
    else:
        bin_list = []
        default_lst = []
        for i in range(n):
            word = input()
            default_lst.append(word)
            uppr_word = word.upper()
            bin_list.append((uppr_word, i))
            bin_list.sort()
        print(default_lst[bin_list[0][1]])