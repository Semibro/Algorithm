class PriorityQueue {
    constructor() {
        this.heap = [];
    }
    
    enqueue(node, dist) {
        this.heap.push({ node, dist });
        this.heapifyup(this.heap.length - 1);
    }
    
    heapifyup(index) {
        while (index > 0) {
            const parentIndex = (index - 1) >> 1;
            if (this.heap[parentIndex].dist <= this.heap[index].dist) break;
            [this.heap[parentIndex], this.heap[index]] = [this.heap[index], this.heap[parentIndex]];
            index = parentIndex;
        }
    }
    
    dequeue() {
        const min = this.heap[0];
        const end = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.heapifydown(0);
        }
        return min;
    }
    
    heapifydown(index) {
        while (index < this.heap.length) {
            const left = (index << 1) + 1;
            const right = (index << 1) + 2;
            let smallest = index;
            if (this.heap[left] && this.heap[left].dist < this.heap[smallest].dist) {
                smallest = left;
            }
            if (this.heap[right] && this.heap[right].dist < this.heap[smallest].dist) {
                smallest = right;
            }
            if (smallest === index) break;
            [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
            index = smallest;
        }
    }
    
    isEmpty() {
        return this.heap.length === 0;
    }
}

function solution(N, road, K) {
    let answer = 1;
    const graph = Array.from({ length: N + 1 }, () => []);
    const INF = Infinity;
    const distance = Array(N + 1).fill(INF);
    
    for (let index = 0; index < road.length; index++) {
        const [a, b, c] = road[index];
        graph[a].push([b, c]);
        graph[b].push([a, c]);
    }
    
    function dijkstra(start) {
        const pQueue = new PriorityQueue();
        pQueue.enqueue(start, 0);
        distance[start] = 0;
        
        while (!pQueue.isEmpty()) {
            let { node, dist } = pQueue.dequeue();
            
            if (distance[node] < dist) continue;
            
            for (let [adj, cost] of graph[node]) {
                let totalCost = distance[node] + cost;
                if (distance[adj] > totalCost) {
                    distance[adj] = totalCost;
                    pQueue.enqueue(adj, totalCost);
                }
            }
        }
    }
    
    dijkstra(1);
    
    for (let index = 2; index <= N; index++) {
        if (distance[index] <= K) {
            answer += 1;
        }
    }
    
    return answer;
}