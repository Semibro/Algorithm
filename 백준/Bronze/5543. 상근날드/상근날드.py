hamburger = []
for _ in range(3):
    hamburger.append(int(input()))
beverage = []
for _ in range(2):
    beverage.append(int(input()))
print(min(hamburger)+min(beverage)-50)