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
