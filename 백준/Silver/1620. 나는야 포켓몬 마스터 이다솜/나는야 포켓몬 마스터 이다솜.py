import sys
n, m = map(int, sys.stdin.readline().split())
pokemon_lst = {} # 시간복잡도 해결을 위한 딕셔너리

for i in range(1, n+1):
    pokemon = sys.stdin.readline().rstrip()
    pokemon_lst[i] = pokemon # 딕셔너리에 포켓몬 추가
    pokemon_lst[pokemon] = i

for j in range(m):
    answer = sys.stdin.readline().rstrip()
    if str.isdigit(answer):
        print(pokemon_lst[int(answer)])
    else:
        print(pokemon_lst[answer])