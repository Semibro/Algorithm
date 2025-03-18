import java.io.*;
import java.util.*;

public class Main {
    static List<String> cards;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        cards = Arrays.asList(br.readLine().split(" "));
        
        int M = Integer.parseInt(br.readLine());
        String[] noCards = br.readLine().split(" ");
        
        Collections.sort(cards);
        int mid = N / 2;
        
        for (int i = 0; i < M; i++) {
            if (binarySearch(noCards[i])) {
                System.out.print("1 ");
            } else {
                System.out.print("0 ");
            }
        }
    }
    
    static boolean binarySearch(String value) {
        int left = 0, right = cards.size() - 1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            int cmp = cards.get(mid).compareTo(value);
            
            if (cmp == 0) {
                return true;
            } else if (cmp < 0) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return false;
    }
}