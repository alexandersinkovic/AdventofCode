f = open("Day_6_2019.txt", "r")
for x in f:
    lst = x[0:-1:].split(")")
    print(lst)

d = {}
for x in lst:
    try:
        d[x[0]] = d[x[0]] + x[1]
    except:
        d[x[0]] = x[1]

#fg = {abc, 3fg}