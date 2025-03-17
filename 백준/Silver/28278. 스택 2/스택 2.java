import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        Deque<String> deque = new ArrayDeque<>();
        
        for (int i = 0; i < N; i++) {
            String[] values = br.readLine().split(" ");
            
            if (values[0].equals("1") && values.length > 1) {
                deque.addLast(values[1]);
            } else if (values[0].equals("2")) {
                if (deque.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(deque.pollLast());
                }
            } else if (values[0].equals("3")) {
                System.out.println(deque.size());
            } else if (values[0].equals("4")) {
                if (deque.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else {
                if (deque.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(deque.peekLast());
                }
            }
        }
    }
}