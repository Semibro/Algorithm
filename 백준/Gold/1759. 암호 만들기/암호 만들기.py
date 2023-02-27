def recur(leng, n):
    if leng == L:  # 길이가 L과 같아질때
        m = j = 0  # m:모음 / j:자음
        for i in range(L): # L만큼 for문 작동
            if result[i] in moum:  # 해당값이 모음자음인지 체크
                m += 1
            else:
                j += 1
        if m >= 1 and j >= 2:  # 모음 1개 이상 자음 2개 이상
            print(''.join(result))  # 그 때만 프린트
        return
    for i in range(n, C):  # 백트래킹
            result.append(lst[i])  # lst의 값 하나 추가
            recur(leng+1, i+1)  # 값 증가
            result.pop()  # 백트래킹은 원상복구가 필수!

L, C = map(int, input().split())
lst = sorted(list(input().split()))  # 처음부터 sort해서 저장
moum = ['a', 'e', 'i', 'o', 'u']  # 모음 모음..ㅎ
result = []
recur(0, 0)