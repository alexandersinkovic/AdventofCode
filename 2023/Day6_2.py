t = 47847467
for j in range(t):
    td = j * (t-j)
    if td > 207139412091014:
        print(t - (j*2) + 1)
        break