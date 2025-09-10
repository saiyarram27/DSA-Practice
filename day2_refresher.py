# day 2 python refresher
# check for duplicate characters in a string
def contains_duplicates(a):
  return len(a) != len(set(a))
print(contains_duplicates("hello"))
print(contains_duplicates("hanuma"))

# count the number of vowels using filter
def count_vowels(a):
  l = list(filter(lambda x: x.lower() in ('a', 'e', 'i', 'o', 'u'), a))
  return len(l)
print(count_vowels('Hanuma REddy'))

#Use list comprehension to get squares of numbers divisible by 3
l = list(range(40))
l2 = [x ** 2 for x in l if x % 3 == 0]
print(l2)
