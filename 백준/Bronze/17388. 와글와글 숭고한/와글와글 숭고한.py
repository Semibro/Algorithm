S, K, H = map(int, input().split())
if S + K + H >= 100:
    print("OK")
else:
    if S == min(S, K, H):
        print('Soongsil')
    elif K == min(S, K, H):
        print('Korea')
    else:
        print('Hanyang')