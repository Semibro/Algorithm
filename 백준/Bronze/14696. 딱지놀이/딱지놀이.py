round = int(input())
for _ in range(round):
    a, *a_lst = map(int, input().split())
    b, *b_lst = map(int, input().split())
    a_lst = list(a_lst)
    b_lst = list(b_lst)
    if a_lst.count(4) > b_lst.count(4):
        print('A')
    elif a_lst.count(4) < b_lst.count(4):
        print('B')
    else:
        if a_lst.count(3) > b_lst.count(3):
            print('A')
        elif a_lst.count(3) < b_lst.count(3):
            print('B')
        else:
            if a_lst.count(2) > b_lst.count(2):
                print('A')
            elif a_lst.count(2) < b_lst.count(2):
                print('B')
            else:
                if a_lst.count(1) > b_lst.count(1):
                    print('A')
                elif a_lst.count(1) < b_lst.count(1):
                    print('B')
                else:
                    print('D')