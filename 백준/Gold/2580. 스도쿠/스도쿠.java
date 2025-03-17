import java.io.*;

public class Main {
    static int[][] board = new int[9][9];
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        for (int i = 0; i < 9; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < 9; j++) {
                board[i][j] = Integer.parseInt(input[j]);
            }
        }
        
        solve(0, 0);
        
        printBoard();
    }
    
    static void printBoard() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }
    
    static boolean solve(int row, int col) {
        if (row == 9) {
            return true;
        }
        
        int nextRow = (col == 8) ? row + 1 : row;
        int nextCol = (col + 1) % 9;
        
        if (board[row][col] != 0) {
            return solve(nextRow, nextCol);
        }
        
        for (int num = 1; num <= 9; num++) {
            if (isValid(row, col, num)) {
                board[row][col] = num;
                if (solve(nextRow, nextCol)) {
                    return true;
                }
                board[row][col] = 0;
            }
        }
        
        return false;
    }
    
    static boolean isValid(int row, int col, int num) {
        // 가로,세로 탐색
        for (int idx = 0; idx < 9; idx++) {
            if (board[row][idx] == num || board[idx][col] == num) {
                return false;
            }
        }
        
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[startRow + i][startCol + j] == num) {
                    return false;
                }
            }
        }
        
        return true;
    }
}