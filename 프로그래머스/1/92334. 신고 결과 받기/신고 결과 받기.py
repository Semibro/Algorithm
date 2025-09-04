from collections import defaultdict

def solution(id_list, report, k):
    report_count = defaultdict(int)
    report_dict = defaultdict(set)
    answer = [0] * len(id_list)
    
    for r in report:
        a, b = r.split(" ")
        if b not in report_dict[a]:
            report_count[b] += 1
            report_dict[a].add(b)
        
    for key in report_count.keys():
        if report_count[key] >= k:
            for i in report_dict.keys():
                if key in report_dict[i]:
                    answer[id_list.index(i)] += 1
                    
    return answer