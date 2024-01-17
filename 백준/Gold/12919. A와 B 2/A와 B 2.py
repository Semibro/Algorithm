S = input()
T = input()
answer = 0

def check_string(input_value):
    global answer
    if answer == 1:
        return

    if len(input_value) == 0:
        return

    if input_value == S:
        answer = 1
        return

    if input_value[-1] == 'A':
        check_string(input_value[:-1])
    if input_value[0] == 'B':
        check_string(input_value[1:][::-1])

check_string(T)
print(answer)