function solution(nums) {
    const N = nums.length;
    const pokemon = {};
    
    for (const num of nums) {
        if (!pokemon[num]) {
            pokemon[num] = 1
        } else {
            pokemon[num] += 1
        }
    }
    
    if (Object.keys(pokemon).length >= N / 2) {
        return N / 2;
    } else {
        return Object.keys(pokemon).length;
    }
}