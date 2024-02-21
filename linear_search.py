def linear_search(array, search_value):
    """Linear Search implementation"""

    # Iterate through every element in the array
    for value in array:

        # If value is found return its index
        if value == search_value:
            return array.index(value)

    # If value not found return None
    return None


print(linear_search([1, 3, 2, 7, 9, 5], 1))
