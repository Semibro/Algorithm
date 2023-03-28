N = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_v, min_v = -1000000001, 1000000001

def recur(num, plus, minus, mul, div, idx):
    global max_v, min_v
    if idx == N:
        max_v = max(num, max_v)
        min_v = min(num, min_v)
        return
    else:
        if plus > 0:
            recur(num+number[idx], plus-1, minus, mul, div, idx+1)
        if minus > 0:
            recur(num-number[idx], plus, minus-1, mul, div, idx+1)
        if mul > 0:
            recur(num*number[idx], plus, minus, mul-1, div, idx+1)
        if div > 0:
            recur(int(num/number[idx]), plus, minus, mul, div-1, idx+1)

recur(number[0], operator[0], operator[1], operator[2], operator[3], 1)
print(max_v)
print(min_v)