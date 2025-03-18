import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        List<Integer> A = Arrays.stream(br.readLine().split(" "))
                                .map(Integer::parseInt)
                                .sorted()
                                .collect(Collectors.toList());

        List<Integer> B = Arrays.stream(br.readLine().split(" "))
                                .map(Integer::parseInt)
                                .sorted(Comparator.reverseOrder())
                                .collect(Collectors.toList());
        
        int S = 0;
        for (int i = 0; i < N; i++) {
            S += A.get(i) * B.get(i);
        }
        
        System.out.print(S);
    }
}