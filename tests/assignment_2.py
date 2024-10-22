from tests.assignment_1 import most_frequent_element

# ASSIGNMENT 2
"""
Test case 1:
    - Check when input is not a list
Input data:
    - Number 0
Expected result:
    - Message "Invalid input. Input must be a list" is displayed
"""
nums_1 = 0
result_1 = most_frequent_element(nums_1)
print("Test case 1\n" + f"Output: {result_1}\n")

"""
Test case 2:
    - Check when list is empty
Input data:
    - Empty list
Expected result:
    - Message "Invalid input. List must be not empty" is displayed
"""
nums_2 = []
result_2 = most_frequent_element(nums_2)
print("Test case 2\n" + f"Output: {result_2}\n")

"""
Test case 3:
    - Check when list has more than 100 elements
Input data:
    - List has 101 elements below
Expected result:
    - Message "Invalid input. Total number of elements must not be more than 100" is displayed
"""
nums_3 = [4, 8, 9, 1, 7, 9, 6, 0, 6, 8, 0, 3, 5, 5, 1, 7, 8, 1, 5, 4, 9, 2, 1, 0, 3, 2, 1, 5, 5, 6, 3, 5, 3, 7, 5, 5, 3, 8, 6, 6, 2, 8, 5, 1, 8, 0, 0, 6, 2, 9, 6, 6, 5, 9, 0, 4, 7, 5, 3, 2, 4, 6, 3, 5, 8, 0, 1, 9, 3, 0, 1, 7, 3, 0, 8, 6, 8, 4, 5, 4, 8, 8, 1, 5, 6, 2, 2, 7, 4, 8, 3, 8, 9, 2, 5, 6, 1, 6, 0, 9, 1]
result_3 = most_frequent_element(nums_3)
print("Test case 3\n" + f"Output: {result_3}\n")

"""
Test case 4:
    - Check when list has only 1 element
Input data:
    - List: [5]
Expected result:
    - Return [5]
"""
nums_4 = [5]
result_4 = most_frequent_element(nums_4)
print("Test case 4\n" + f"Output: {result_4}\n")

"""
Test case 5:
    - Check when List has many elements, only 1 element with the highest frequency
Input data:
    - List: [1, 1, 1, 2, 2, 5, 5, 5, 7, 7, 7, 7, 7, 9]
Expected result:
    - Return [7]
"""
nums_5 = [1, 1, 1, 2, 2, 5, 5, 5, 7, 7, 7, 7, 7, 9]
result_5 = most_frequent_element(nums_5)
print("Test case 5\n" + f"Output: {result_5}\n")

"""
Test case 6:
    - Check when List has many elements, more than 1 element with the highest frequency
Input data:
    - List: [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6]
Expected result:
    - Return [1, 3, 5]
"""
nums_6 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6]
result_6 = most_frequent_element(nums_6)
print("Test case 6\n" + f"Output: {result_6}\n")

"""
Test case 7:
    - Check when list has an element that is not a number from 0 to 9
Input Data:
    - List: [1, 2, 10, 2, 1]
Expected result:
    - Message "Invalid input. List must have numbers from 0 to 9 only" is displayed
"""
nums_7 = [1, 2, 10, 2, 1]
result_7 = most_frequent_element(nums_7)
print("Test case 7\n" + f"Output: {result_7}\n")
