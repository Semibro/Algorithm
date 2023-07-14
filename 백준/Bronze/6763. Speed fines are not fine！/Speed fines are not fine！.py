A = int(input())
B = int(input())

if A >= B:
    print('Congratulations, you are within the speed limit!')
else:
    if B-A <= 20:
        print('You are speeding and your fine is $100.')
    elif B-A <= 30:
        print('You are speeding and your fine is $270.')
    else:
        print('You are speeding and your fine is $500.')