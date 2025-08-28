# are given an array of integers, nums, and an integer target.

# Your task is to determine if there exist two distinct elements in nums whose sum is exactly equal to target.

# You may not use the same element twice.

# Input Format

# The input will be provided as follows:

# The first line contains an integer N, representing the number of elements in the array.

# The second line contains N space-separated integers, representing the elements of the array nums.

# The third line contains a single integer, target.

# Constraints

# 2≤nums.length≤10 5

# −10^9 ≤nums[i]≤10^9

# −10^9 ≤target≤10^9

# Output Format

# Return a boolean value:

# true if a pair of numbers summing to the target exists.

# false otherwise.

# Example 1:

# Given nums = [2, 7, 11, 15] and target = 9, the output should be true because nums[0] + nums[1] = 2 + 7 = 9.

# Example 2:

# Given nums = [3, 5, 8, 10] and target = 12, the output should be false as no two numbers in the array sum to 12.

# Sample Input 0

# 4
# 2 7 11 15
# 9
# Sample Output 0

# true
# Sample Input 1

# 4
# 3 5 8 10
# 12
# Sample Output 1

# false

def two_sum_exists(nums, target):
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False


N = int(input().strip())
nums = list(map(int, input().split()))
target = int(input().strip())

# Output
print(str(two_sum_exists(nums, target)).lower())  #TC:O[n]   SC:O[n]