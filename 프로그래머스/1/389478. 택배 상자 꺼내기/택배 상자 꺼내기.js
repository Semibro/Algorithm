// 택배상자 개수 : n, 가로로 놓는 상자 개수 : w, 꺼내려는 택배 상자 번호 : num
function solution(n, w, num) {
    let maxLength;
    if (n % w) {
        maxLength = n + (w - (n % w));
    } else {
        maxLength = n;
    }
    const boardTopLength = Math.floor(n / w) + 1;
    const board = Array.from({ length: boardTopLength }, () => []);
    let index = 1;
    
    for (i = 1; i <= maxLength; i++) {
        if (index % 2 == 0) {
            if (i > n) {
                board[index-1].unshift(0);
            } else {
                board[index-1].unshift(i);
            }
            if (board[index-1].length >= w) {
                index++;
            }
        } else {
            if (i > n) {
                board[index-1].push(0);
            } else {
                board[index-1].push(i);
            }
            if (board[index-1].length >= w) {
                index++;
            }
        }
    }
    
    let answer = 0;
    for (i = 0; i < boardTopLength; i++) {
        for (j = 0; j < w; j++) {
            if (board[i][j] == num) {
                for (k = i; k < boardTopLength; k++) {
                    if (board[k][j]) answer += 1;
                }
            }
        }
    }
    
    return answer;
}