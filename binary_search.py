def binary_search(array, search_value):
    """Binary Search implementation"""

    # Establish lower and upper bounds
    lower_bound = 0
    upper_bound = len(array) - 1

    # Loop where we inspect the middlemost value between upper and lower bounds
    while lower_bound <= upper_bound:

        # Find the midpoint with the "//" integer division operator
        midpoint = (upper_bound + lower_bound) // 2

        # Inspect value at midpoint
        value_at_midpoint = array[midpoint]

        # If the value is the one we are looking for we are done
        # If value at midpoint is lower we change the lower bound to middle + 1
        # If value at midpoint is greater we change the upper bound to middle -1

        if search_value == value_at_midpoint:
            return midpoint
        elif search_value > value_at_midpoint:
            lower_bound = midpoint + 1
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1

    # If we narrow the bounds until they reach each other, that means the value
    # is not in the array, so we return "None"
    return None


numbers = [1, 2, 3, 4, 5, 6]

print(binary_search(numbers, 3))
