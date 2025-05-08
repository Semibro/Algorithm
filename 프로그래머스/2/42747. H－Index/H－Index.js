function solution(citations) {
    let answer = 0;
    citations.sort((a, b) => b-a);
    for (let index = 0; index < citations.length; index++) {
        if (index+1 > citations[index]) {
            return index;
        }
    }
    
    return citations.length;
}