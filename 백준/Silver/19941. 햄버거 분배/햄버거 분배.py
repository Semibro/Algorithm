N, K = map(int, input().split())
hamburger = input()  # P: 사람 / H: 햄버거
check = [0] * N
count = 0

for i in range(N):
    if hamburger[i] == 'P':
        ch = True
        if i-K < 0:
            for j in range(0, i):
                if hamburger[j] == 'H' and check[j] == 0:
                    count += 1
                    check[j] = 1
                    ch = False
                    break
        else:
            for j in range(i-K, i):
                if hamburger[j] == 'H' and check[j] == 0:
                    count += 1
                    check[j] = 1
                    ch = False
                    break
        if ch:
            if i+1+K > N:
                for j in range(i+1, N):
                    if hamburger[j] == 'H' and check[j] == 0:
                        count += 1
                        check[j] = 1
                        break
            else:
                for j in range(i+1, i+1+K):
                    if hamburger[j] == 'H' and check[j] == 0:
                        count += 1
                        check[j] = 1
                        break

print(count)