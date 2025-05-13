class Queue {
    constructor() {
        this.store = {};
        this.front = 0;
        this.rear = 0;
    }
    
    size() {
        if (this.store[this.rear] === undefined) {
            return 0;
        } else {
            return this.rear - this.front + 1;
        }
    }
    
    push(data) {
        if (this.size() !== 0) {
            this.rear += 1;
        }
        this.store[this.rear] = data;
    }
    
    popleft() {
        let temp = this.store[this.front];
        delete this.store[this.front];
        
        if (this.front === this.rear) {
            this.front = 0;
            this.rear = 0;
        } else {
            this.front += 1;
        }
        
        return temp;
    }
    
    peekfront() {
        if (this.size() === 0) {
            return undefined;
        } else {
            return this.store[this.front];
        }
    }
    
    peekrear() {
        if (this.size() === 0) {
            return undefined;
        } else {
            return this.store[this.rear];
        }
    }
}

// function solution(land) {
//     let answer = 0;
//     const row = land.length;
//     const col = land[0].length;
//     const direction = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    
//     for (let y = 0; y < col; y++) {
//         let oilCount = 0;
//         const visited = Array.from({ length: row }, () => Array(col).fill(false));
//         const queue = new Queue();
        
//         for (let x = 0; x < row; x++) {
//             if (land[x][y] === 1 && !visited[x][y]) {
//                 visited[x][y] = true;
//                 queue.push([x, y]);
//                 oilCount += 1;
                
//                 while (queue.size() > 0) {
//                     const current = queue.popleft();
//                     const currentX = current[0];
//                     const currentY = current[1];
                    
//                     for (const d of direction) {
//                         const nextX = currentX + d[0];
//                         const nextY = currentY + d[1];
                        
//                         if (nextX >= 0 && nextX < row && nextY >= 0 && nextY < col) {
//                             if (land[nextX][nextY] === 1 && !visited[nextX][nextY]) {
//                                 queue.push([nextX, nextY]);
//                                 visited[nextX][nextY] = true;
//                                 oilCount += 1;
//                             }
//                         }
//                     }
//                 }
//             }
//         }
        
//         answer = Math.max(answer, oilCount);
//     }
    
//     return answer;
// }
function solution(land) {
    const row = land.length;
    const col = land[0].length;
    const visited = Array.from({ length: row }, () => Array(col).fill(false));
    const direction = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    const oilPerColumn = Array(col).fill(0);

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (land[i][j] === 1 && !visited[i][j]) {
                const queue = new Queue();
                queue.push([i, j]);
                visited[i][j] = true;

                let oilCount = 1;
                const columns = new Set();
                columns.add(j);

                while (queue.size() > 0) {
                    const [x, y] = queue.popleft();
                    
                    for (const [dx, dy] of direction) {
                        const nx = x + dx;
                        const ny = y + dy;

                        if (nx >= 0 && nx < row && ny >= 0 && ny < col) {
                            if (land[nx][ny] === 1 && !visited[nx][ny]) {
                                queue.push([nx, ny]);
                                visited[nx][ny] = true;
                                oilCount += 1;
                                columns.add(ny);
                            }
                        }
                    }
                }

                // 연결된 열들에 이 덩어리의 석유량을 더해줍니다.
                for (const colIdx of columns) {
                    oilPerColumn[colIdx] += oilCount;
                }
            }
        }
    }

    return Math.max(...oilPerColumn);
}