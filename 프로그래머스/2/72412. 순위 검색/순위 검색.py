# 효율성 달설 실패 코드
# def solution(info, query):
#     answer = []
    
#     for q in query:
#         language, _, job, _, career, _, food, X  = q.split(" ")
#         count = 0
        
#         for i in info:
#             l, j, c, f, p = i.split(" ")
#             if language == l or language == "-":
#                 if job == j or job == "-":
#                     if career == c or career == "-":
#                         if food == f or food == "-":
#                             if int(p) >= int(X):
#                                 count += 1
                                
#         answer.append(count)
    
#     return answer

from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    # info를 dict 형태로 저장
    info_dict = defaultdict(list)
    for i in info:
        items = i.split(" ")
        condition = items[:-1]
        score = int(items[-1])
        
        # 조건 조합 생성
        for n in range(5):
            for comb in combinations(range(4), n):
                temp = condition[:]
                for index in comb:
                    temp[index] = "-"
                key = " ".join(temp)
                info_dict[key].append(score)
                
    # 각 key의 점수를 정렬 (이분 탐색 진행을 위함)
    for scores in info_dict.values():
        scores.sort()
        
    # query 처리
    answer = []
    for q in query:
        language, _, job, _, career, _, food, X  = q.split(" ")
        key = f"{language} {job} {career} {food}"
        target = int(X)
        
        if key in info_dict:
            scores = info_dict[key]
            # 이분 탐색
            idx = bisect_left(scores, target)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
    
    return answer