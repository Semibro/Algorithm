alphabat = input()
bin_list = []

for i in range(len(alphabat)):
    bin_list.append(ord(alphabat[i]) - 64)

print(*bin_list)