from collections import defaultdict

W, S = map(int, input().split())
W_content = input()
S_content = input()
W_count = defaultdict(int)
S_count = defaultdict(int)
W_len = len(W_content)
answer = 0

for char in W_content:
    W_count[char] += 1
        
for i in range(W_len):
    S_count[S_content[i]] += 1
        
def is_valid():
    for key in W_count.keys():
        if S_count[key] != W_count[key]:
            return False
    return True

if is_valid():
    answer += 1
    
for i in range(W_len, len(S_content)):
    out_char = S_content[i - W_len]
    in_char = S_content[i]
    S_count[out_char] -= 1
    S_count[in_char] += 1
    
    if is_valid():
        answer += 1
        
print(answer)