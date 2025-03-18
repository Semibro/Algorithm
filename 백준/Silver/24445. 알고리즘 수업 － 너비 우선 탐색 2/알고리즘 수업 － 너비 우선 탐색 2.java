import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int R = Integer.parseInt(input[2]);
        
        List<Integer>[] graph = new ArrayList[N + 1];
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
        
        // 내림차순 정렬
        for (int i = 1; i < N + 1; i++) {
            graph[i].sort(Collections.reverseOrder());
        }
        
        //BFS
        Deque<Integer> deque = new ArrayDeque<>();
        int[] visited = new int[N + 1];
        
        deque.addLast(R);
        int count = 1;
        visited[R] = count++;
        
        while (!deque.isEmpty()) {
            int node = deque.pollFirst();
            for (int nextNode: graph[node]) {
                if (visited[nextNode] == 0) {
                    deque.addLast(nextNode);
                    visited[nextNode] = count++;
                }
            }
        }
        
        for (int i = 1; i < N + 1; i++) {
            System.out.println(visited[i]);
        }
    }
}