import java.io.*;
import java.util.*;

public class Main {
    static int count;
    static boolean[] visited;
    static List<Integer>[] graph;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        
        graph = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < M; i++) {
            String[] item = br.readLine().split(" ");
            int a = Integer.parseInt(item[0]);
            int b = Integer.parseInt(item[1]);
            graph[b].add(a);
        }
        
        int[] answer = new int[N + 1];
        int maxCount = 0;
        
        for (int i = 1; i < N + 1; i++) {
            visited = new boolean[N + 1];
            count = 0;
            dfs(i);
            
            answer[i] = count;
            maxCount = Math.max(maxCount, count);
        }
        
        StringBuilder computer = new StringBuilder();
        for (int i = 1; i < N + 1; i++) {
            if (maxCount == answer[i]) {
                computer.append(i + " ");
            }
        }
        
        System.out.print(computer);
    }
    
    static void dfs(int node) {
        visited[node] = true;
        count++;
        
        for (int nextNode: graph[node]) {
            if (!visited[nextNode]) {
                dfs(nextNode);
            }
        }
    }
}