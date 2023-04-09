def solution(picks, minerals):
    global res
    res = 9876543210
    fatigue = [(1, 1, 1), (5, 1, 1), (25, 5, 1)]
    mine = {'diamond':0, 'iron':1, 'stone':2}

    def bt(idx, dia, iron, stone, mineral, cnt):
        global res
        if idx >= len(mineral) or (dia == 0 and iron == 0 and stone == 0):
            res = min(res, cnt)
            return
        else:
            dia_cnt, iron_cnt, stone_cnt = 0, 0, 0
            for i in range(idx, min(idx+5, len(mineral))):
                dia_cnt += fatigue[0][mine[mineral[i]]]
                iron_cnt += fatigue[1][mine[mineral[i]]]
                stone_cnt += fatigue[2][mine[mineral[i]]]
            if dia:
                bt(idx+5, dia-1, iron, stone, mineral, cnt+dia_cnt)
            if iron:
                bt(idx+5, dia, iron-1, stone, mineral, cnt+iron_cnt)
            if stone:
                bt(idx+5, dia, iron, stone-1, mineral, cnt+stone_cnt)
            
    bt(0, picks[0], picks[1], picks[2], minerals, 0)
    return res