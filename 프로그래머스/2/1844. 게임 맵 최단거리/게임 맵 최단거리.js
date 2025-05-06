function solution(maps) {
    let answer = -1;
    
    const direction = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    const row = maps.length;
    const col = maps[0].length;
    const visited = Array.from({ length: row }, () => Array(col).fill(0));
    
    const deque = [];
    deque.push([0, 0]);
    visited[0][0] = 1;
    
    while (deque.length > 0) {
        const currentXY = deque.shift();
        for (let index = 0; index < 4; index++) {
            const nextX = currentXY[0] + direction[index][0];
            const nextY = currentXY[1] + direction[index][1];
            
            if (0 <= nextX && nextX < row && 0 <= nextY && nextY < col && maps[nextX][nextY] === 1 && visited[nextX][nextY] === 0) {
                deque.push([nextX, nextY]);
                visited[nextX][nextY] = visited[currentXY[0]][currentXY[1]] + 1;
            }
        }
    }
    
    if (visited[row-1][col-1] === 0) {
        return answer;
    } else {
        return visited[row-1][col-1];
    }
}