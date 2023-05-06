l = [(1,2,5),(3,4,6)]
am = 5
d = dict(zip([i[0] for i in l], [h[1]*am for h in l]))
print(d)