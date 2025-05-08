function solution(numbers) {
    let answer = "";
    const stringNumbers = [];
    for (const number of numbers) {
        stringNumbers.push(number.toString());
    }
    
    stringNumbers.sort(function(a, b) {
        const one = a + b;
        const two = b + a;
        if (one < two) return 1;
        else if (one > two) return -1;
        else return 0;
    });
    
    if (stringNumbers[0] === "0") return "0";
    
    for (const stringNumber of stringNumbers) {
        answer += stringNumber;
    }
    
    return answer;
}