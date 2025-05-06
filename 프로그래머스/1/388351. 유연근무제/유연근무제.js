function solution(schedules, timelogs, startday) {
    // 출근가능 시간으로 스케쥴 변경
    for (let index = 0; index < schedules.length; index++) {
        const minute = schedules[index] % 100;
        if (minute + 10 >= 60) {
            let time = Math.floor(schedules[index] / 100);
            time *= 100;
            time += 100;
            time += minute - 50;
            schedules[index] = time;
        } else {
            schedules[index] += 10
        }
    }
    
    let answer = 0;
    
    for (let i = 0; i < schedules.length; i++) {
        let checkCount = 0;
        for (let j = 0; j < 7; j++) {
            if (startday < 6 && timelogs[i][j] <= schedules[i]) {
                checkCount += 1;
            }
            startday += 1;
            if (startday === 8) {
                startday = 1;
            }
        }
        
        if (checkCount === 5) {
            answer += 1;
        }
    }
    
    return answer
}