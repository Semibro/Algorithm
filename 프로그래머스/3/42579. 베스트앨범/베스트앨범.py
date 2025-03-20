def solution(genres, plays):
    answer = []
    genres_play_total_count = {}
    genres_index_play = {}
    
    for idx in range(len(genres)):
        g = genres[idx]
        p = plays[idx]
        
        if g in genres_index_play:
            genres_play_total_count[g] += p
            genres_index_play[g].append((idx, p))
        else:
            genres_play_total_count[g] = p
            genres_index_play[g] = [(idx, p)]

    sorted_plays = sorted(genres_play_total_count.items(), key = lambda x: -x[1])
    
    for genre, total_play in sorted_plays:
        sorted_genre = sorted(genres_index_play[genre], key = lambda x: (-x[1], x[0]))
        if len(sorted_genre) > 1:
            answer.append(sorted_genre[0][0])
            answer.append(sorted_genre[1][0])
        else:
            answer.append(sorted_genre[0][0])
            
    return answer