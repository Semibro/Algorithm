import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int d = Integer.parseInt(input[1]);
        int k = Integer.parseInt(input[2]);
        int c = Integer.parseInt(input[3]);

        
        // 회전초밥 만들기
        int[] sushi = new int[N];
        for (int i = 0; i < N; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }
        
        // 슬라이딩 윈도우
        HashMap<Integer, Integer> window = new HashMap<>();
        int maxCount = 0;
        
        // 윈도우 초기 설정
        for (int i = 0; i < k; i++) {
            window.put(sushi[i], window.getOrDefault(sushi[i], 0) + 1);
        }
        
        // 쿠폰 초밥 추가
        window.put(c, window.getOrDefault(c, 0) + 1);
        maxCount = window.size();
        
        // 슬라이딩 윈도우 이동
        for (int i = 1; i < N; i++) {
            int removeSushi = sushi[i - 1];
            if (window.get(removeSushi) == 1) {
                window.remove(removeSushi);
            } else {
                window.put(removeSushi, window.get(removeSushi) - 1);
            }
            
            int addSushi = sushi[(i + k - 1) % N];
            window.put(addSushi, window.getOrDefault(addSushi, 0) + 1);
            
            maxCount = Math.max(maxCount, window.size());
        }
                         
        System.out.print(maxCount);
    }
}