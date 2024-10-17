def solution(k, tangerine):
    answer = 0
    countDict = {}
    
    for item in tangerine:
        if item in countDict:
            countDict[item] += 1
        else:
            countDict[item] = 1
            
    sortedList = sorted(countDict.items(), key = lambda x: x[1], reverse = True)
    
    for i in range(len(sortedList)):
        k -= sortedList[i][1]
        answer += 1
        if k <= 0:
            break
    
    return answer