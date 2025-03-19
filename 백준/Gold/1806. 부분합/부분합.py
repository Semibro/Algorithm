N, S = map(int, input().split())
elements = list(map(int, input().split()))

for i in range(1, N):
    elements[i] = elements[i] + elements[i-1]

answer = 100000
left, right = 0, 0

while left <= right and right < N:
    if left == 0 and elements[right] >= S:
        answer = min(answer, right + 1)
        left += 1

    if elements[right] - elements[left] >= S:
        answer = min(answer, right - left)
        left += 1
    else:
        right += 1

if answer == 100000:
    print(0)
else:
    print(answer)