from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    user_to_idx = { user_id: i for i, user_id in enumerate(id_list) }
    
    reported_counts = defaultdict(int)
    reporter_map = defaultdict(set)
    
    for r in set(report):
        reporter, reported = r.split()
        reported_counts[reported] += 1
        reporter_map[reporter].add(reported)
        
    for reporter, reported_set in reporter_map.items():
        mail_count = 0
        for reported_user in reported_set:
            if reported_counts[reported_user] >= k:
                mail_count += 1
        
        answer[user_to_idx[reporter]] = mail_count
            
    return answer
