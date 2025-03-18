import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = input.length();
        
        // 전체 a개수 구하기
        int aCount = 0;
        for (int i = 0; i < n; i++) {
            if (input.charAt(i) == 'a') {
                aCount++;
            }
        }
        
        // 원형임을 고려하며 확장
        String extended = input + input;
        
        // aCount 크기의 윈도우에서 b의 개수 구하기
        int bCount = 0;
        for (int i = 0; i < aCount; i++) {
            if (extended.charAt(i) == 'b') {
                bCount++;
            }
        }
        
        // 최소 교환 개수 구하기
        int min = bCount;
        for (int i = 1; i < n; i++) {
            if (extended.charAt(i - 1) == 'b') {
                bCount--;
            }
            if (extended.charAt(i + aCount - 1) == 'b') { 
                bCount++;
            }
            min = Math.min(min, bCount);
        }
        
        System.out.print(min);
    }
}