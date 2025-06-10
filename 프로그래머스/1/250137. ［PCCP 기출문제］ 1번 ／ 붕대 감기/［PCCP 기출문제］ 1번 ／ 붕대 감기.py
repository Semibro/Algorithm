# bandage = [시전 시간, 초당 회복량, 추가 회복량]
# health = 최대 체력
# attacks = [공격 시간, 피해량], 공격 시간을 기준으로 오름차순 정렬된 상태

def solution(bandage, health, attacks):
    casting_time, recovery_amount_per_second, additional_recovery_amount = bandage[0], bandage[1], bandage[2]
    last_time = attacks[-1][0]
    current_health, attack_index, bandage_count = health, 0, 0
    
    for time in range(1, last_time+1):
        if time < attacks[attack_index][0]:
            bandage_count += 1
            if bandage_count == casting_time:
                current_health += additional_recovery_amount
                bandage_count = 0
            current_health += recovery_amount_per_second
        elif time == attacks[attack_index][0]:
            current_health -= attacks[attack_index][1]
            bandage_count = 0
            if current_health <= 0:
                return -1
            attack_index += 1
        
        if current_health > health:
            current_health = health
            
    return current_health    