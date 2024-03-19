"""
Linear Search implementation
src: Discrete Mathematics and Its Application
"""


def linear_search(x, arr):
    n = len(arr)
    i = 0
    while i < n and x != arr[i]:
        i += 1

    if i < n:
        return i
    else:
        return -1


numbers = [1, 3, 2, 7, 9, 5]

print(linear_search(3, numbers))
