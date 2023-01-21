n = int(input())
number_list = list(map(int, input().split()))
count = 0

def is_prime_number(number):
  if number == 1:
    pass
  else:
    for i in range(2, number):
      if number % i == 0:
        return False
    return True

for i in number_list:
  if is_prime_number(i):
    count += 1

print(count)