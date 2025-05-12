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
        if (this.size() === 0) {
            this.store["0"] = data;
        } else {
            this.rear += 1;
            this.store[this.rear] = data;
        }
    }
    
    popleft() {
        let temp;
        if (this.front === this.rear) {
            temp = this.store[this.front];
            delete this.store[this.front];
            this.front = 0;
            this.rear = 0;
            return temp;
        } else {
            temp = this.store[this.front];
            delete this.store[this.front];
            this.front += 1;
            return temp;
        }
    }
}

function solution(maps) {
    let answer = -1;
    
    const direction = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    const row = maps.length;
    const col = maps[0].length;
    const visited = Array.from({ length: row }, () => Array(col).fill(0));
    
    const queue = new Queue();
    queue.push([0, 0]);
    visited[0][0] = 1;
    
    while (queue.size() > 0) {
        const currentXY = queue.popleft();
        for (let index = 0; index < 4; index++) {
            const nextX = currentXY[0] + direction[index][0];
            const nextY = currentXY[1] + direction[index][1];
            
            if (0 <= nextX && nextX < row && 0 <= nextY && nextY < col && maps[nextX][nextY] === 1 && visited[nextX][nextY] === 0) {
                queue.push([nextX, nextY]);
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