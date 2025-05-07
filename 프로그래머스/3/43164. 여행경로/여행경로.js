function solution(tickets) {
    let answer = [];
    let graph = {};
    
    for (let [from, to] of tickets) {
        if (!graph[from]) graph[from] = [];
        graph[from].push(to);
    }
    
    for (let from in graph) {
        graph[from].sort();
    }
    
    function dfs(current, route, usedCount) {
        route.push(current);
        
        if (usedCount === tickets.length) {
            answer = [...route];
            return true;
        }
        
        if (!graph[current]) {
            route.pop();
            return false;
        }
        
        for (let index = 0; index < graph[current].length; index++) {
            const next = graph[current][index];
            if (next === null) continue;
            
            graph[current][index] = null;
            if (dfs(next, route, usedCount+1)) return true;
            graph[current][index] = next;
        }
        
        route.pop();
        return false;
    }
    
    dfs("ICN", [], 0);
    return answer;
}