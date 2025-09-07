# find the frequency of elements in a list
l = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
d = {x: l.count(x) for x in set(l)}
print(d)
