x = input()
for i in range(len(x)//2):
    if x[i] != x[-(i+1)]:
        print(0)
        break
else:
    print(1)