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
            this.store[this.rear] = data;
        } else {
            this.rear += 1;
            this.store[this.rear] = data;
        }
    }
    
    popLeft() {
        let popData = this.store[this.front];
        delete this.store[this.front];
        
        if (this.front === this.rear) {
            this.front = 0;
            this.rear = 0;
        } else {
            this.front += 1;
        }
        
        return popData;
    }
    
    peekFront() {
        if (this.size() === 0) {
            return undefined;
        } else {
            return this.store[this.front];
        }
    }
    
    peekRear() {
        if (this.size() === 0) {
            return undefined;
        } else {
            return this.store[this.rear];
        }
    }
}

function solution(rectangle, characterX, characterY, itemX, itemY) {
    const boardSize = 102;
    const board = Array.from({ length: boardSize }, () => Array(boardSize).fill(0));
    
    for (const r of rectangle) {
        const x1 = r[0] * 2;
        const y1 = r[1] * 2;
        const x2 = r[2] * 2;
        const y2 = r[3] * 2;
        
        for (let i = x1; i < x2 + 1; i++) {
            for (let j = y1; j < y2 + 1; j++) {
                board[i][j] = 1;
            }
        }
    }
    
    for (const r of rectangle) {
        const x1 = r[0] * 2;
        const y1 = r[1] * 2;
        const x2 = r[2] * 2;
        const y2 = r[3] * 2;
        
        for (let i = x1 + 1; i < x2; i++) {
            for (let j = y1 + 1; j < y2; j++) {
                board[i][j] = -1;
            }
        }
    }
    
    const startX = characterX * 2;
    const startY = characterY * 2;
    const endX = itemX * 2;
    const endY = itemY * 2;
    
    const direction = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    const visited = Array.from({ length: boardSize }, () => Array(boardSize).fill(0));
    const queue = new Queue();
    
    visited[startX][startY] = 1;
    queue.push([startX, startY]);
    
    while (queue.size() > 0) {
        const current = queue.popLeft();
        const currentX = current[0];
        const currentY = current[1];
        
        if (currentX === endX && currentY === endY) {
            return Math.floor((visited[currentX][currentY] - 1) / 2);
        }
        
        for (const d of direction) {
            const nextX = currentX + d[0];
            const nextY = currentY + d[1];
            
            if (nextX >= 0 && nextX < 102 && nextY >= 0 && nextY < 102) {
                if (visited[nextX][nextY] === 0 && board[nextX][nextY] === 1) {
                    queue.push([nextX, nextY]);
                    visited[nextX][nextY] = visited[currentX][currentY] + 1;
                }
            }
        }
    }
}