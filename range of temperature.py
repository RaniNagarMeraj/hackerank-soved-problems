# modern manufacturing plant, a series of N sensors monitor the temperature of a critical machine. For the machine to operate safely, its temperature must stay within a "normal" range, which is defined as being between 20 and 80 degrees, inclusive.

# Any reading that falls outside this range is considered an anomaly and requires attention. You need to write a program that processes a list of temperature readings and provides a summary report with two key numbers:

# The total count of readings that are within the normal operating range.

# The total count of readings that are anomalies (either below 20 or above 80).

# Input Format

# The first line will contain a single integer, N, representing the total number of sensor readings.

# The second line will contain N space-separated integers, representing the temperature reading from each sensor.

# Example: Input:

# 8 25 75 15 85 50 90 30 60

# Explanation: The list of temperature readings is [25, 75, 15, 85, 50, 90, 30, 60].

# The readings within the normal range [20, 80] are 25, 75, 50, 30, 60. The count is 5.

# The anomalous readings outside the range are 15, 85, 90. The count is 3.

# Output:

# 5 3

# Constraints

# 1 leN le100

# 0 le texttemperaturereading le150

# Output Format

# Print two space-separated integers on a single line: the count of normal readings, followed by the count of anomalous readings.

# Sample Input 0

# 8  
# 25 75 15 85 50 90 30 60
# Sample Output 0

# 5 3
# Sample Input 1

# 5  
# 20 30 40 50 80
# Sample Output 1

# 5 0




# Read number of readings
N = int(input())

# Read temperature readings as a list of integers
readings = list(map(int, input().split()))

# Initialize counters
normal_count = 0
anomaly_count = 0

# Check each reading
for temp in readings:
    if 20 <= temp <= 80:
        normal_count += 1
    else:
        anomaly_count += 1

# Output the counts
print(normal_count, anomaly_count)