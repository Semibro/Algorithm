function solution(points, routes) {
    function findMax(arr) {
        let maxValue = -Infinity;
        for (const point of arr) {
            maxValue = Math.max(maxValue, point[0], point[1]);
        }
        return maxValue;
    }
    
    let answer = 0;
    const maxBoardSize = findMax(points);
    const board = Array.from({ length: maxBoardSize + 1 }, () => Array.from({ length: maxBoardSize + 1 }, () => []));
    
    for (let routeId = 0; routeId < routes.length; routeId++) {
        const route = routes[routeId];
        let moveCount = 0;   // route별로 moveCount 초기화

        for (let index = 0; index < route.length - 1; index++) {
            const [sr, sc] = points[route[index] - 1];
            const [er, ec] = points[route[index + 1] - 1];

            let r = sr, c = sc;
            board[r][c].push({ routeId, time: moveCount });

            while (r !== er) {
                r += (er > r) ? 1 : -1;
                moveCount++;
                board[r][c].push({ routeId, time: moveCount });
            }
            while (c !== ec) {
                c += (ec > c) ? 1 : -1;
                moveCount++;
                board[r][c].push({ routeId, time: moveCount });
            }
        }
    }
    
    for (let i = 0; i <= maxBoardSize; i++) {
        for (let j = 0; j <= maxBoardSize; j++) {
            const visits = board[i][j];
            if (visits.length > 1) {
                const timeMap = new Map();

                for (const { routeId, time } of visits) {
                    if (!timeMap.has(time)) {
                        timeMap.set(time, new Set());
                    }
                    timeMap.get(time).add(routeId);
                }

                for (const routeSet of timeMap.values()) {
                    if (routeSet.size >= 2) {
                        answer += 1;
                    }
                }
            }
        }
    }
    
    return answer;
}