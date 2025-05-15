S, P = map(int, input().split())
DNA = input()
required = list(map(int, input().split()))
answer = 0
current_count = { "A": 0, "C": 0, "G": 0, "T": 0 }

for i in range(P):
    current_count[DNA[i]] += 1
    
def is_valid():
    for index, char in enumerate("ACGT"):
        if current_count[char] < required[index]:
            return False
    return True

if is_valid():
    answer += 1
   
for i in range(P, S):
    out_char = DNA[i - P]
    in_char = DNA[i]
    current_count[out_char] -= 1
    current_count[in_char] += 1
    
    if is_valid():
        answer += 1
        
print(answer)