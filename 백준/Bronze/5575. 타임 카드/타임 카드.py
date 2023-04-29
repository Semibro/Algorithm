for _ in range(3):
    ch, cm, cs, th, tm, ts = map(int, input().split())
    if ts >= cs:
        rs = ts-cs
    else:
        rs = 60+ts-cs
        tm -= 1
    if tm >= cm:
        rm = tm-cm
    else:
        rm = 60+tm-cm
        th -= 1
    rh = th-ch
    print(f'{rh} {rm} {rs}')