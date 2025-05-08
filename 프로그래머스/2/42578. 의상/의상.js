function solution(clothes) {
    let answer = 1;
    const clothesType = {};
    
    for (const cloth of clothes) {
        if (!clothesType[cloth[1]]) {
            clothesType[cloth[1]] = 1;
        } else {
            clothesType[cloth[1]] += 1;
        }
    }
    
    for (const type in clothesType) {
        answer *= (clothesType[type] + 1);
    }
    
    return answer - 1;
}