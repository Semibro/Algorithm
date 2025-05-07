function solution(bridge_length, weight, truck_weights) {
    let answer = 0;
    let bridge = Array(bridge_length).fill(0);
    let currentWeight = 0;
    
    while (truck_weights.length > 0 || currentWeight > 0) {
        answer += 1;
        
        let exitedTruck = bridge.shift();
        currentWeight -= exitedTruck;
        
        let nextTruck = truck_weights[0];
        if (nextTruck && currentWeight + nextTruck <= weight) {
            bridge.push(nextTruck);
            currentWeight += nextTruck;
            truck_weights.shift();
        } else {
            bridge.push(0);
        }
    }
    
    return answer;
}