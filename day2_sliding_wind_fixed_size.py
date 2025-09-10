# day2 sliding window basics (fixed size)

#Max sum of subarray of size k
def max_sum_subarray(nums, k):
  max_sum = sum(nums[:k])
  for i in range(k, len(nums)):
    current_sum = max_sum - nums[i - k] + nums[i]
    max_sum =  max(max_sum, current_sum)
  return max_sum

print(max_sum_subarray([1,4,5,6,7,8,3,1,2,5,8,4,2], 5))

#Min sum of subarray of size k
def min_sum_subarray(nums, k):
  min_sum = sum(nums[: k])
  for i in range(k, len(nums)):
    current_sum = min_sum - nums[i - k] + nums[i]
    min_sum = min(min_sum, current_sum)
  return min_sum
print(min_sum_subarray([1,4,5,6,7,8,3,1,2,5,8,4,2], 5))


# Find all subarrays of size k in a list
def find_subarrays(nums, k):
  l = []
  window = nums[:k]
  l.append(tuple(window))
  for i in range(k, len(nums)):
    window = window[1:] + [nums[i]]
    l.append(tuple(window))
  return l

print(find_subarrays([x for x in range(11)], 5))

# Return their sums in a list
def find_sums(l):
  l_sum = list(map(lambda x: sum(x), l))
  return l_sum

print(find_sums(find_subarrays([x for x in range(11)], 5)))
