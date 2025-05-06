function solution(n, computers) {
    let answer = 0;
    
    const visited = Array(n).fill(false);
    for (let index = 0; index < n; index++) {
        if (!visited[index]) {
            answer += 1;
            
            const deque = [index];
            while (deque.length > 0) {
                const currentNode = deque.shift();
                
                for (let nodeIndex = 0; nodeIndex < n; nodeIndex++) {
                    if (!visited[nodeIndex] && currentNode != nodeIndex && computers[currentNode][nodeIndex] === 1) {
                        deque.push(nodeIndex);
                        visited[nodeIndex] = true;
                    }
                }
            }
        }
    }
    
    return answer;
}