N = int(input())
lst = list(map(int, input().split()))
answer = [0] * N

for i in range(N):
    cnt = 0  # 내가 들어갈 자리를 찾는 변수 (0의 개수를 세자!)
    for j in range(N):
        # 나의 앞에 큰 수가 없고, 정답 리스트가 비어있으면 넣자!
        if lst[i] == 0 and answer[j] == 0:
            answer[j] += i+1
            break
        # 나의 앞에 큰 수가 1개라도 있을 때
        if lst[i] != 0:
            if cnt == lst[i] and answer[j] == 0:
                answer[j] += i+1
                break
            if cnt < lst[i] and answer[j] == 0:
                cnt += 1

print(*answer)