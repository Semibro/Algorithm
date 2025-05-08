function solution(routes) {
    let answer = 1;
    
    if (routes.length === 1) return answer;
    
    const sortedRoutes = routes.sort(function(a, b) {
        if (a[1] > b[1]) return 1;
        if (a[1] < b[1]) return -1;
        if (a[1] === b[1]) return 0;
    });
    
    let outRoute = sortedRoutes[0][1];
    let index = 1;
    
    while (index < sortedRoutes.length) {
        if (outRoute >= sortedRoutes[index][0] && outRoute <= sortedRoutes[index][1]) {
            index += 1
        } else {
            answer += 1;
            outRoute = sortedRoutes[index][1];
            index += 1;
        }
    }
    
    return answer;
}