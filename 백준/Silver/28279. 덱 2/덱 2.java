import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        Deque<String> deque = new ArrayDeque<>();
        
        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            
            if (input[0].equals("1") && input.length > 1) {
                deque.addFirst(input[1]);
            } else if (input[0].equals("2") && input.length > 1) {
                deque.addLast(input[1]);
            } else if (input[0].equals("3")) {
                if (deque.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(deque.pollFirst());
                }
            } else if (input[0].equals("4")) {
                if (deque.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(deque.pollLast());
                }
            } else if (input[0].equals("5")) {
                System.out.println(deque.size());
            } else if (input[0].equals("6")) {
                if (deque.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else if (input[0].equals("7")) {
                if (deque.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(deque.peekFirst());
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