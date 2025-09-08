# list comprehension - it's a simple way to create lists using single line of code instead of using loops

# traditional way
l = []
for i in range(1, 6):
  l.append(i)
print(l)

# using set comprehension
m = [n for n in range(1, 6)]
print(m)

# list comprehension with condition
n = [x for x in range(15) if x % 2 == 0]# adding a condition for even numbers
print(n)

# nested list comprehension
two_d = [[1,2], [3,4]]
one_d = [x for row in two_d for x in row]
print(one_d)

# applying a function inside comprehension
words = ['apple', 'banana', 'grapes']
u = [w.upper() for w in words]
print(u)


""" Lambda function - its a anonymous nameless function 
that takes one or more inputs or parameters, 
but only has one expression( result that is automatically returned)"""

# basic example for lambda function
f = lambda x: x ** 2
print(f(5))

# multiple arguments, parameters, or inputs
add = lambda a, b: a + b
print(add(3, 4))

# with map function
nums = [1,2,3,4,5]
l = list(map(lambda x: x ** 2 , nums))
print(l)

# with filter function
nums = [x for x in range(21)]
e = list(filter(lambda x: x % 2 == 0, nums))
print(e)

# with sorted and key
d = {"a": 5, "b": 4, "c": 3, "d": 2, "e": 1}
sorted_dictionary  = dict(sorted(d.items(), key = lambda x: x[1]))
print(sorted_dictionary)

# practice 

# converting a 2d list to 1d list using list comprehension
a = [[1,2,3], [4,5,6]]
b = [x for row in a for x in row]
print(b)

# sort the list of tuples by second value using the lambda
v = [(10,20), (2,5),(6,2)]
u = [n for n in sorted(v, key = lambda x: x[1])]
print(u)

# filter the even numbers from a list of numbers using filter and lambda
nums = [x for x in range(31)]
filtered = list(filter(lambda x: x % 2 == 0, nums))
print(filtered)
