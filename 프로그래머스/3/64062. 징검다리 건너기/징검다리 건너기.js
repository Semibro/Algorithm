function solution(stones, k) {    
    // 건널 수 있는지 여부 판단 함수
    function canCross(peopleCount) {
        let count = 0;
        for (let i = 0; i < stones.length; i++) {
            if (stones[i] - peopleCount < 0) {
                count++;
                if (count >= k) return false;
            } else {
                count = 0;
            }
        }
        return true;
    }
    
    // 이분 탐색
    let left = 1;
    let right = stones[0];
    for (let s of stones) {
        if (s > right) right = s;
    }
    let answer = 0;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (canCross(mid)) {
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return answer;
}