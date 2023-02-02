while True:
    result = 'YES'
    nx, ny, w = input().split()
    nx = int(nx)
    ny = int(ny)
    w = float(w)
    if nx + ny + w == 0:
        break
    else:
        nx_lst = list(map(float, input().split()))
        ny_lst = list(map(float, input().split()))
        nx_lst.append(-w/2)
        nx_lst.append(75+w/2)
        ny_lst.append(-w/2)
        ny_lst.append(100+w/2)
        sort_nx_lst = sorted(nx_lst)
        sort_ny_lst = sorted(ny_lst)
        for i in range(len(sort_nx_lst) - 1):
            if result == 'YES' and sort_nx_lst[i+1] - sort_nx_lst[i] > w:
                result = 'NO'
                break
        for j in range(len(sort_ny_lst) - 1):
            if result == 'YES' and sort_ny_lst[j+1] - sort_ny_lst[j] > w:
                result = 'NO'
                break
        print(result)