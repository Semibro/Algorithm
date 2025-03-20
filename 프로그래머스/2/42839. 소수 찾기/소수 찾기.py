from itertools import permutations

def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    number_list = set()
    
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            number_list.add(int("".join(perm)))
            
    for number in number_list:
        if isPrime(number):
            answer += 1
            
    return answer