function solution(players, m, k) {
    let answer = 0;
    const serverSchedule = Array(24).fill(0);
    
    for (let hour = 0; hour < 24; hour++) {
        let activeServers = 0;
        for (let time = Math.max(0, hour-k+1); time <= hour; time++) {
            activeServers += serverSchedule[time];
        }
        
        const needServers = Math.floor(players[hour] / m);
        
        if (activeServers < needServers) {
            const additionalServers = needServers - activeServers;
            serverSchedule[hour] = additionalServers;
            answer += additionalServers;
        }
    }
    
    return answer;
}