import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static int[] visited;
    static int count;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int R = Integer.parseInt(input[2]);
        
        graph = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < M; i++) {
            String[] node = br.readLine().split(" ");
            int u = Integer.parseInt(node[0]);
            int v = Integer.parseInt(node[1]);
            graph[u].add(v);
            graph[v].add(u);
        }
        
        for (int i = 1; i < N + 1; i++) {
            Collections.sort(graph[i], Collections.reverseOrder());
        }
        
        visited = new int[N + 1];
        count = 1;
        dfs(R);
        
        for (int i = 1; i < N + 1; i++) {
            System.out.println(visited[i]);
        }
    }
    
    /*
    static void dfs(int startNode) {
        Deque<Integer> deque = new ArrayDeque<>();
        
        deque.addLast(startNode);
        visited[startNode] = count;
        
        while (!deque.isEmpty()) {
            int node = deque.pollLast();
            
            for (int nextNode: graph[node]) {
                if (visited[nextNode] == 0) {
                    count++;
                    visited[nextNode] = count;
                    deque.addLast(nextNode);
                }
            }
        }
    }
    */
    
    static void dfs(int node) {
        visited[node] = count++;
        
        for (int nextNode: graph[node]) {
            if (visited[nextNode] == 0) {
                dfs(nextNode);
            }
        }
    }
}