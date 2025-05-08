function solution(genres, plays) {
    const answer = [];
    const N = genres.length;
    const playTotalTime = {};
    const genresPlayTime = {};
    
    for (let index = 0; index < N; index++) {
        if (!playTotalTime[genres[index]]) {
            playTotalTime[genres[index]] = plays[index];
            genresPlayTime[genres[index]] = [[plays[index], index]];
        } else {
            playTotalTime[genres[index]] += plays[index];
            genresPlayTime[genres[index]].push([plays[index], index]);
        }
    }
    
    const sortedPlayTotalTime = Object.entries(playTotalTime).sort((a, b) => b[1] - a[1]);
    
    for (const genreAndTime of sortedPlayTotalTime) {
        const genre = genreAndTime[0];
        const sortedGenrePlayTime = genresPlayTime[genre].sort(function(a, b) {
            if (a[0] > b[0]) return -1;
            else if (a[0] < b[0]) return 1;
            else {
                if (a[1] > b[1]) return 1;
                else return -1;
            }
        });
        
        console.log(sortedGenrePlayTime);
        
        if (sortedGenrePlayTime.length === 1) {
            answer.push(sortedGenrePlayTime[0][1]);
        } else if (sortedGenrePlayTime.length >= 2) {
            answer.push(sortedGenrePlayTime[0][1]);
            answer.push(sortedGenrePlayTime[1][1]);
        }
    }
    
    return answer;
}