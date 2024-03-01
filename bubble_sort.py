def bubble_sort(arr):
    """Bubble sort implementation"""

    unsorted_until_index = len(arr) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(unsorted_until_index):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
        unsorted_until_index -= 1

    return arr


numbers = [1, 3, 2, 7, 9, 5]

print(bubble_sort(numbers))
