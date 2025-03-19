import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        
        for (int i = 1; i < 2 * N; i++) {
            if (i <= N) {
                System.out.println(" ".repeat(N - i) + "*".repeat(2 * i -1));
            } else {
                System.out.println(" ".repeat(i - N) + "*".repeat(2 * (2 * N - i) -1));
            }
        }
    }
}