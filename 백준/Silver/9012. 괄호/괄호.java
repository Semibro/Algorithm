import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < T; i++) {
            String input = br.readLine();
            Deque<Character> deque = new ArrayDeque<>();
            boolean invalid = true;
            
            for (int j = 0; j < input.length(); j++) {
                if (input.charAt(j) == '(') {
                    deque.addLast('(');
                } else {
                    if (!deque.isEmpty()) {
                        deque.pollLast();
                    } else {
                        System.out.println("NO");
                        invalid = false;
                        break;
                    }
                }
            }
            
            if (invalid) {
                if (deque.isEmpty()) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
    }
}