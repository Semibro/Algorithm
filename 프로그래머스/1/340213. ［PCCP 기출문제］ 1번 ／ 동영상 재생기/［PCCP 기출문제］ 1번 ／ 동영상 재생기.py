def change_time(time):
    splited_time = time.split(":")
    minute, second = int(splited_time[0]), int(splited_time[1])
    return minute * 60 + second

def return_change_time(time):
    minute = str(time // 60)
    second = str(time % 60)
    return f"{minute.zfill(2)}:{second.zfill(2)}"
    

def solution(video_len, pos, op_start, op_end, commands):
    # change time minute to second
    changed_video_len, changed_pos, changed_op_start, changed_op_end = change_time(video_len), change_time(pos), change_time(op_start), change_time(op_end)
    
    # start commands
    for command in commands:
        # 오프닝 건너뛰기
        if changed_pos >= changed_op_start and changed_pos <= changed_op_end:
            changed_pos = changed_op_end
        
        # prev
        if command == "prev":
            if changed_pos < 10:
                changed_pos = 0
            else:
                changed_pos -= 10
                
        # next
        if command == "next":
            if changed_pos + 10 >= changed_video_len:
                changed_pos = changed_video_len
            else:
                changed_pos += 10
                
        # 오프닝 건너뛰기
        if changed_pos >= changed_op_start and changed_pos <= changed_op_end:
            changed_pos = changed_op_end
            
    return return_change_time(changed_pos)