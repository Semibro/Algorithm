function solution(diffs, times, limit) {
    let left = 1;
    let right = diffs.reduce((acc,cur) => Math.max(acc, cur), 1);
    
    function calcDiff(mid) {
        let result = 0;
        
        for (let index = 0; index < diffs.length; index++) {
            if (mid < diffs[index]) {
                const mistakeCount = diffs[index] - mid;
                const prevTime = index > 0 ? times[index-1] : 0;
                result += mistakeCount * (times[index] + prevTime);
            }
            result += times[index];
            if (result > limit) {
                return false;
            }
        }
        
        return result <= limit;
    }
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (calcDiff(mid)) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return left;
}