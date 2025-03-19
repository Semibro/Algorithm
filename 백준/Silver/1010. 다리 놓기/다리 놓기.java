import java.io.*;
import java.util.*;

public class Main {
    static int[][] dp = new int[30][30];
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
        int T = Integer.parseInt(br.readLine());
        
        for (int t = 0; t < T; t++) {
            String[] input = br.readLine().split(" ");
            int N = Integer.parseInt(input[0]);
            int M = Integer.parseInt(input[1]);
            
            System.out.println(dpFunc(M, N));
        }
    }
    
    static int dpFunc(int m, int n) {
        if (n == m) {
            return 1;
        }
        
        if (n > m) {
            return 0;
        }
        
        if (n < 0 || m < 0) {
            return 0;
        }
        
        if (dp[m][n] > 0) {
            return dp[m][n];
        }
        
        return dp[m][n] = dpFunc(m - 1, n - 1) + dpFunc(m - 1, n);
    }
}