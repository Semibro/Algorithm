n = int(input())
def fibonachi(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonachi(num-2) + fibonachi(num-1)
print(fibonachi(n))