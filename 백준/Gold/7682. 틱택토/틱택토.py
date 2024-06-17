# 승자 선택 함수
def check_winner(user, board):
    # 행 검사
    if user == board[0] or user == board[1] or user == board[2]:
        return True
    # 열 검사
    if user == board[0][0]+board[1][0]+board[2][0] or user == board[0][1]+board[1][1]+board[2][1] or user == board[0][2]+board[1][2]+board[2][2]:
        return True
    # 대각선 검사
    if user == board[0][0]+board[1][1]+board[2][2] or user == board[0][2]+board[1][1]+board[2][0]:
        return True
    # 틱택토 실패
    return False

# 틱택토 함수
def tictactoe(item):
    # 개수 파악 (count O / count X / count .)
    CO, CX, CD = item.count('O'), item.count('X'), item.count('.')
    # 틱택토 보드
    board = [item[:3], item[3:6], item[6:]]

    # X가 이긴 경우
    if CX == CO+1 and check_winner('XXX', board) and check_winner('OOO', board) == False:
        return True
    # O가 이긴 경우
    if CX == CO and check_winner('OOO', board) and check_winner('XXX', board) == False:
        return True
    # 무승부인 경우
    if CD == 0 and CX == CO+1 and check_winner('XXX', board) == False and check_winner('OOO', board) == False:
        return True
    # 위 경우를 모두 벗어나는 케이스
    return False


while True:
    T = input()

    # end는 종료조건
    if T == 'end':
        break

    # 틱택토
    if tictactoe(T):
        print('valid')
    else:
        print('invalid')