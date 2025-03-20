def solution(nums):
    pokemon = {}
    
    for num in nums:
        if num in pokemon:
            pokemon[num] += 1
        else:
            pokemon[num] = 1
            
    if len(nums) // 2 <= len(pokemon):
        return len(nums) // 2
    else:
        return len(pokemon)