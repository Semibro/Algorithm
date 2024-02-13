N = int(input())
solution = list(map(int, input().split()))

left_index, left_answer = 0, 0
right_index, right_answer = N-1, N-1
check = 9876543210

while left_index < right_index:
    temp_value = solution[left_index] + solution[right_index]

    if abs(temp_value) < check:
        check = abs(temp_value)
        left_answer = left_index
        right_answer = right_index

    if temp_value == 0:
        break
    elif temp_value < 0:
        left_index += 1
    else:
        right_index -= 1

print(solution[left_answer], solution[right_answer])