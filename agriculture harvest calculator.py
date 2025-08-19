# In a unique grove in a remote village, a farmer has planted a single row of N magical trees. These trees are of two alternating types:
# Sunfruit Trees: Located at the even positions in the row (index 0, 2, 4, ...). The total yield of Sunfruit is calculated by adding the number of fruits from each Sunfruit tree.
# Moonpetal Trees: Located at the odd positions in the row (index 1, 3, 5, ...). The magical potency of these trees is calculated by multiplying the number of petals from each Moonpetal tree.
# You are tasked with creating a program that takes a list of yields from each tree and calculates two final values: the total Sunfruit yield (the sum) and the total Moonpetal potency (the product).
# Input Format
# The first line will contain a single integer, N, representing the total number of trees.
# The second line will contain N space-separated integers, representing the yield of each tree in the row.
# Constraints
# 1 leN le20
# 1 le textyieldofeachtree le10
# Output Format
# Print two space-separated integers on a single line: the total sum of yields from even-indexed trees, followed by the total product of yields from odd-indexed trees. If there are no odd-indexed trees, the product should be considered 1.
# Example:
# Input:
# 6
# 5 2 3 4 8 3
# Explanation: The list of yields is [5, 2, 3, 4, 8, 3].
# # The yields at even indices (0, 2, 4) are 5, 3, and 8. Their sum is 5+3+8=16.
# The yields at odd indices (1, 3, 5) are 2, 4, and 3. Their product is 2 times4 times3=24.
# Output:
# 16 24

# Read number of trees
n = int(input("enter the number of trres:"))

# Read yields of each tree
yields = list(map(int, input("enter numbers sseperated by spaces:").split()))

# Initialize sum for even indices (Sunfruit) and product for odd indices (Moonpetal)
sum_even = 0
product_odd = 1

for i in range(n):
    if i % 2 == 0:  # Even index → Sunfruit tree
        sum_even += yields[i]
    else:           # Odd index → Moonpetal tree
        product_odd *= yields[i]

# Print results
print(sum_even, product_odd)


