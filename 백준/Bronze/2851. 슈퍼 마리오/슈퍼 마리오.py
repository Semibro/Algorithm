mushroom = [int(input()) for _ in range(10)]
for i in range(1, 10):
    mushroom[i] += mushroom[i-1]

answer = 0
for i in range(10):
    if abs(100-answer) >= abs(100-mushroom[i]):
        answer = mushroom[i]
        
print(answer)