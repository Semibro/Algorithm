function solution(n, arr1, arr2) {
    const answer = [];
    
    function changeBinaryNumber(num) {
        if (num.length < n) {
            const temp = n - num.length;
            let res = "";
            
            for (let i = 0; i < temp; i++) {
                res += "0";
            }
            
            res += num;
            return res;
        } else {
            return num;
        }
    }
    
    for (let i = 0; i < n; i++) {
        const map1 = changeBinaryNumber(arr1[i].toString(2));
        const map2 = changeBinaryNumber(arr2[i].toString(2));
        let res = "";
        
        for (let j = 0; j < n; j++) {
            if (map1[j] === "1" || map2[j] === "1") {
                res += "#";
            } else {
                res += " ";
            }
        }
        
        answer.push(res);
    }
    
    return answer;
}