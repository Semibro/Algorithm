t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    board = [input().split() for _ in range(n)]
    check_1, check_2, count = 0, 0, 0

    for j in range(n):
      check_1 = 0
      check_2 = 0
      for m in range(n):
        if board[j][m] == '1':
          check_1 += 1
          if check_1 == k:
            if m == n-1:
              count += 1
              check_1 = 0
            else:
              if board[j][m+1] == '0':
                count += 1
                check_1 = 0
              elif board[j][m+1] == '1':
                pass
          elif check_1 > k:
            pass
          else:
            pass
        else:
          check_1 = 0
        if board[m][j] == '1':
          check_2 += 1
          if check_2 == k:
            if m == n-1:
              count += 1
              check_2 = 0
            else:
              if board[m+1][j] == '0':
                count += 1
                check_2 = 0
              elif board[m+1][j] == '1':
                pass
          elif check_2 > k:
            pass
          else:
            pass
        else:
          check_2 = 0
    print(f'#{i+1} {count}')