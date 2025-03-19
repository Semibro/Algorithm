import java.io.*;
import java.util.*;

public class Main {
    static int answer = 0;
    static List<Integer>[] graph;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] input = br.readLine().split(" ");
        int N =  Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        
        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < M; i++) {
            String[] nodes = br.readLine().split(" ");
            int a = Integer.parseInt(nodes[0]);
            int b = Integer.parseInt(nodes[1]);
            
            graph[a].add(b);
            graph[b].add(a);
        }
        
        for (int i = 0; i < N; i++) {
            if (answer == 0) {
                boolean[] visited = new boolean[N];
                visited[i] = true;
                dfs(i, 1, visited);
            }
        }
        
        System.out.print(answer);
    }
    
    static void dfs(int node, int count, boolean[] visited) {
        if (count == 5) {
            answer = 1;
            return;
        }
        
        for (int nextNode: graph[node]) {
            if (!visited[nextNode]) {
                count = count + 1;
                visited[nextNode] = true;
                dfs(nextNode, count, visited);
                count = count - 1;
                visited[nextNode] = false;
            }
        }
    }
}