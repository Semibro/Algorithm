function solution(video_len, pos, op_start, op_end, commands) {
    // video_len
    const splitedVideoLen = video_len.split(":");
    const videoLen = parseInt(splitedVideoLen[0]) * 60 + parseInt(splitedVideoLen[1]);
    // pos
    const splitedPosLen = pos.split(":");
    let posLen = parseInt(splitedPosLen[0]) * 60 + parseInt(splitedPosLen[1]);
    // op_start
    const splitedOpStartLen = op_start.split(":");
    const opStartLen = parseInt(splitedOpStartLen[0]) * 60 + parseInt(splitedOpStartLen[1]);
    // op_end
    const splitedOpEndLen = op_end.split(":");
    const opEndLen = parseInt(splitedOpEndLen[0]) * 60 + parseInt(splitedOpEndLen[1]);
    
    for (const command of commands) {
        if (posLen >= opStartLen && posLen <= opEndLen) posLen = opEndLen;
        
        if (command === "next") {
            const nextPosLen = posLen + 10;
            
            if (nextPosLen >= videoLen) {
                posLen = videoLen;
            } else {
                posLen = nextPosLen;
            }
        } else {
            const prevPosLen = posLen - 10;
            
            if (prevPosLen <= 0) {
                posLen = 0;
            } else {
                posLen = prevPosLen;
            }
        }
        
        if (posLen >= opStartLen && posLen <= opEndLen) posLen = opEndLen;
    }
    
    let answer = "";
    const hour = Math.floor(posLen / 60).toString().length === 1 ? "0" + Math.floor(posLen / 60).toString() : Math.floor(posLen / 60).toString();
    const minute = (posLen % 60).toString().length === 1 ? "0" + (posLen % 60).toString() : (posLen % 60).toString();
    answer = hour + ":" + minute;
    
    return answer;
}