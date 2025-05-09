function solution(info, n, m) {
    let answer = Infinity;
    const itemLength = info.length;
    const visited = new Set();
    
    function dfs(index, aSum, bSum) {
        if (aSum >= n || bSum >= m) return;
        
        if (index === itemLength) {
            answer = Math.min(answer, aSum);
            return;
        }
        
        const key = `${index}-${aSum}-${bSum}`;
        if (visited.has(key)) return;
        visited.add(key);
        
        const [aItem, bItem] = info[index];
        
        dfs(index + 1, aSum + aItem, bSum);
        dfs(index + 1, aSum, bSum + bItem);
    }
    
    dfs(0, 0, 0);
    
    return answer === Infinity ? -1 : answer;
}