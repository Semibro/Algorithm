function solution(array, commands) {
    const answer = [];
    
    for (const command of commands) {
        const slicedArray = array.slice(command[0] - 1, command[1]);
        slicedArray.sort((a, b) => a - b);
        answer.push(slicedArray[command[2] - 1])
    }
    
    return answer;
}