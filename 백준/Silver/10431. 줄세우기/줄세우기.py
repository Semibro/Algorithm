for _ in range(int(input())):
    lst = list(map(int, input().split()))  # tc[0]은 테스트케이스 번호
    answer = 0

    for i in range(1, 20):
        for j in range(i+1, 21):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                answer += 1

    print(lst[0], answer)