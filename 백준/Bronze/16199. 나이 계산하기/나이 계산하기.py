by, bm, bd = map(int, input().split())
hy, hm, hd = map(int, input().split())

if bm < hm:
    year1 = hy-by
elif bm == hm and bd <= hd:
    year1 = hy-by
else:
    year1 = hy-by-1
    
year2 = hy-by+1

year3 = hy-by

print(year1, year2, year3, sep='\n')