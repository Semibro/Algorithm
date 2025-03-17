import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        String[] channels = new String[N];
        for (int i = 0; i < N; i++) {
            channels[i] = br.readLine();
        }
        
        
        int kbs1Idx = 0, kbs2Idx = 0;
        for (int j = 0; j < N; j++) {
            if (channels[j].equals("KBS1")) {
                kbs1Idx = j;
            } else if (channels[j].equals("KBS2")) {
                kbs2Idx = j;
            }
        }
        
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < kbs1Idx; i++) {
            result.append("1");
        }
        for (int i = 0; i < kbs1Idx; i++) {
            result.append("4");
        }
        
        if (kbs2Idx < kbs1Idx) {
            kbs2Idx++;
        }
        for (int i = 0; i < kbs2Idx; i++) {
            result.append("1");
        }
        for (int i = 0; i < kbs2Idx - 1; i++) {
            result.append("4");
        }
        
        System.out.println(result);
    }
}