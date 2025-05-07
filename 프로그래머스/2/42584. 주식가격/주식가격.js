function solution(prices) {
    const p = prices;
    const answer = Array(p.length).fill(0);
    const stack = [];
    
    for (let index = 0; index < p.length; index++) {
        while (stack.length && p[index] < p[stack[stack.length-1]]) {
            const currentIndex = stack.pop();
            answer[currentIndex] = index - currentIndex;
        }
        stack.push(index);
    }
    
    while (stack.length) {
        const stackIndex = stack.pop();
        answer[stackIndex] = p.length - 1 - stackIndex;
    }
    
    return answer;
}