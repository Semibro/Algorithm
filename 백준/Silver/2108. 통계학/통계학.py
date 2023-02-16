import sys
ipt = sys.stdin.readline

N = int(ipt().rstrip())
result = []
for _ in range(N):
    a = int(ipt().rstrip())
    result.append(a)

result.sort()
bin_dict = {}
for i in result:
    if i in bin_dict:
        bin_dict[i] += 1
    else:
        bin_dict[i] = 1
max_d = max(bin_dict.values())
bin_list = []
for k, v in bin_dict.items():
    if v == max_d:
        bin_list.append(k)


print(round(sum(result)/N))
print(result[N//2])
if len(bin_list) == 1:
    print(bin_list[0])
else:
    print(bin_list[1])
print(abs(result[0]-result[-1]))