// bandage = [시전 시간(t), 초당 회복량(x), 추가 회복량(y)]
// health = 최대 체력
// attacks = [공격 시간, 피해량]
function solution(bandage, health, attacks) {
    let answer = health;
    const t = bandage[0];
    const x = bandage[1];
    const y = bandage[2];
    let time = 0;
    
    for (const attack of attacks) {
        let heal = 0;
        const healTime = attack[0] - time;
        
        const additionalHeals = Math.floor(healTime / t);
        heal += (x * healTime) + (y * additionalHeals);
        
        if (answer + heal >= health) {
            answer = health;
        } else {
            answer += heal;
        }
        
        answer -= attack[1];
        if (answer <= 0) return -1;
        time = attack[0] + 1;
    }
    
    return answer;
}