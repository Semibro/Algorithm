n = int(input())
number_list = list(map(int, input().split()))
count = 0

# 1이 들어왔을 때는 pass하고 그 외의 숫자에 대한 소수 판별
def is_prime_number(number):
  if number == 1:
    pass
  else:
    for i in range(2, number):
      if number % i == 0:
        return False
    return True

# if문의 True값을 통해 소수면 count에 +1
for i in number_list:
  if is_prime_number(i):
    count += 1

print(count)