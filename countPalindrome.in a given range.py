# You are given two integers, L and R, which represent the inclusive range [L, R]. Your task is to determine how many integers in this range are palindromes.

# A palindrome number is a number that reads the same forward and backward. For example: 121, 44, and 909 are palindromes, while 123 and 450 are not.

# Write a program that:

# Accepts two integers L and R.

# Counts and returns the total number of palindrome numbers between L and R (inclusive).

# Input Format

# The first line contains two integers L and R, separated by a space.

# Constraints

# 1 ≤ L ≤ R ≤ 10⁶

# Output Format

# Print a single integer representing the count of palindrome numbers in the range [L, R].

# Example 1

# Input

# 10 50

# Output

# 4

# Explanation: Palindromes are 11, 22, 33, 44. Actually 4

# Example 2

# Input

# 1 100

# Output

# 18

# Explanation: Palindromes are 1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99.

# Sample Input 0

# 10 50
# Sample Output 0

# 4
# Sample Input 1

# 1 100
# Sample Output 1

# 18


def is_palindrome(n: int) -> bool:
    
    return str(n) == str(n)[::-1]

# Input
L, R = map(int, input().split())

# Count palindromes
count = 0
for num in range(L, R + 1):
    if is_palindrome(num):
        count += 1         #TC:O[R-L+1]
                        #SC:o[1]

print(count)