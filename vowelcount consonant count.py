# esearcher at the "Institute for Ancient Scripts" is studying a newly discovered text. A key part of their analysis involves understanding the phonetic composition of words. To do this, they need a tool that can quickly count the number of vowels and consonants in a given word.

# For this task, the vowels are defined as 'a', 'e', 'i', 'o', 'u'. All other letters are considered consonants.

# You need to write a program that takes a single lowercase word as input and outputs the total count of vowels and consonants.

# Input Format

# The input will be a single line containing a string, S, consisting of lowercase English letters.

# Example: Input:

# programming

# Explanation: The word is "programming".

# The vowels are 'o', 'a', 'i'. The count is 3.

# The consonants are 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g'. The count is 8.

# Output:

# 3 8

# Constraints

# 1 le textlength(S) le1000

# Output Format

# Print two space-separated integers on a single line: the total count of vowels, followed by the total count of consonants.

# Sample Input 0

# programming
# Sample Output 0

# 3 8
# Sample Input 1

# aeiou
# Sample Output 1

# 5 0

# Read the input word
S = input().strip()

# Define the set of vowels
vowels_set = {'a', 'e', 'i', 'o', 'u'}

# Initialize counters
vowels_count = 0
consonants_count = 0

# Count vowels and consonants
for char in S:
    if char in vowels_set:
        vowels_count += 1
    else:
        consonants_count += 1

# Output: vowels count and consonants count
print(vowels_count, consonants_count)