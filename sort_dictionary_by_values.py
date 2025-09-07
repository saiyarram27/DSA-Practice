# sort a dictionary by values
d = {"a": 5, "b": 4, "c": 3, "d": 2, "e": 1}
sorted_dict = dict(__builtin__.sorted(d.items(), key = lambda x: x[1]))
print(sorted_dict)
