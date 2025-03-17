import java.io.*;

public class Main {
    static int N, M;
    static boolean[] visited;
    static int[] result;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        visited = new boolean[N+1];
        result = new int[M];
        
        solve(0);
    }
    
    static void solve(int depth) {
        if (depth == M) {
            for (int num: result) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }
        
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                result[depth] = i;
                solve(depth+1);
                visited[i] = false;
            }
        }
    }
}