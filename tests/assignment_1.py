# ASSIGNMENT 1
def most_frequent_element(nums):
    # Check input
    if nums == []:
        return "Invalid input. List must be not empty"
    if not isinstance(nums, list):
        return "Invalid input. Input must be a list"
    if not all(isinstance(num, int) and 0 <= num <= 9 for num in nums):
        return "Invalid input. List must have numbers from 0 to 9 only"
    if len(nums) > 100:
        return "Invalid input. Total number of elements must not be more than 100"

    # Frequency count
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Find the highest frequency
    max_count = max(counts.values())

    # Find all elements with the highest frequency
    most_frequent = []
    for num, count in counts.items():
        if count == max_count:
            most_frequent.append(num)

    return most_frequent





