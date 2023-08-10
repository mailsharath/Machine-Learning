# Given a list of integers numbers, calculate the pivot index of this list.
# The pivot index is the index where the sum of all the numbers strictly to the left
# of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there
# are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

"""
Asymptotic complexity in terms of length of the given list `n`:
* Time: O(n^2).
* Auxiliary space: O(1).
* Total space: O(n).
"""


def get_pivot_index(numbers):
    # Iterate over all possible pivot indices.
    for i in range(len(numbers)):
        # Calculate the sum of elements to the left of the pivot.
        left_sum = sum(numbers[:i])
        # Calculate the sum of elements to the right of the pivot.
        right_sum = sum(numbers[i + 1:])
        # If the sums are equal, return the current index as the pivot index.
        if left_sum == right_sum:
            return i

    # If no pivot index is found, return -1.
    return -1


numbers1 = [2, 3, 1, -1, 1, 1, 4]

print(get_pivot_index(numbers1))
