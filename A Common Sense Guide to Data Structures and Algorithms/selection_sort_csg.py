"""
Selection Sort Implementation
src: A Common Sense Guide to Data Structures and Algorithms
"""


def selection_sort(arr):
    for i in range(len(arr) - 1):
        lowest_number_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_number_index]:
                lowest_number_index = j

        if lowest_number_index != i:
            temp = arr[i]
            arr[i] = arr[lowest_number_index]
            arr[lowest_number_index] = temp

    return arr


numbers = [1, 3, 2, 7, 9, 5]

print(selection_sort(numbers))
