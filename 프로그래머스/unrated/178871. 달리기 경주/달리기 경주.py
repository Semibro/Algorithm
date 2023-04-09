def solution(players, callings):
    # 딕셔너리를 만들자!
    player_index = {player : i for i, player in enumerate(players)}
    index_player = {i : player for i, player in enumerate(players)}
    
    # 이름이 불림에 따라 순서 변경
    for i in callings:
        now_locate = player_index[i]
        change_locate = now_locate-1
        now_player = i
        change_player = index_player[change_locate]
        # 등수변경
        player_index[now_player] = change_locate
        player_index[change_player] = now_locate
        # 인덱스도 변경
        index_player[now_locate] = change_player
        index_player[change_locate] = now_player
    return list(index_player.values())