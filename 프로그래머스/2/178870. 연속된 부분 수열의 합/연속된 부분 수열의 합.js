function solution(sequence, k) {
    let answer = [];
    
    // 투 포인터
    let endPointer = 0;
    let sequenceSum = 0;
    let sequenceLength = sequence.length;
    let interval = sequence.length;
    
    for (let startPointer = 0; startPointer < sequenceLength; startPointer++) {
        while (endPointer < sequenceLength && sequenceSum < k) {
            sequenceSum += sequence[endPointer];
            endPointer += 1;
        }
        
        if (sequenceSum == k && endPointer-1-startPointer < interval) {
            answer = [startPointer, endPointer-1];
            interval = endPointer - 1 - startPointer;
        }
        
        sequenceSum -= sequence[startPointer];
    }
    
    return answer;
}